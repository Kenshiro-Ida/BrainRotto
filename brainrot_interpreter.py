import re
import sys

# Define tokens including emojis, keywords, and comments
TOKEN_REGEX = [
    ('NUMBER', r'\d+'),
    ('STRING', r'"[^"]*"'),
    ('BOOLEAN', r'\byup\b|\bnah\b'),
    ('ASSIGN', r'\bis\b'),
    ('KEYWORD', r'oi!|check mar|varna|edge till|goon|till|bawe aisa kar ki|bawe ye kar|bawe|wapas la dalle|sun'),
    ('IDENT', r'[a-zA-Z_]\w*'),
    ('COMMENT', r'//[^\n]*'),
    ('OP', r'🔼🟰|🔽🟰|🟰|❌|🔼|🔽|➕|➖|✖️|➗|🤝|🫱|🙅'),
    ('COMMA', r','),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('LBRACE', r'\{'),
    ('RBRACE', r'\}'),
    ('NEWLINE', r'\n'),
    ('SKIP', r'[ \t]+'),
]

def tokenize(code):
    regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_REGEX)
    scanner = re.compile(regex).scanner
    tokens = []
    i = 0
    while i < len(code):
        match = scanner(code, i).match()
        kind = match.lastgroup
        value = match.group()
        if kind not in ('SKIP', 'NEWLINE', 'COMMENT'):
            tokens.append((kind, value))
        i = match.end()
    return tokens

# Interpreter
class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}
        self.returning = None

    def eval_expr(self, expr):
        expr = expr.strip()
        if not expr:
            raise Exception("Empty expression provided.")
        expr = expr.replace("yup", "True").replace("nah", "False")
        expr = expr.replace("sun", "input")
        expr = expr.replace("🔼🟰", ">=").replace("🔽🟰", "<=")
        expr = expr.replace("🟰", "==").replace("❌", "!=")
        expr = expr.replace("🔼", ">").replace("🔽", "<")
        expr = expr.replace("➕", "+").replace("➖", "-")
        expr = expr.replace("✖️", "*").replace("➗", "/")
        expr = expr.replace("🤝", "and").replace("🫱", "or").replace("🙅", "not")
        
        safe_builtins = {"int": int, "float": float, "input": input, "str": str}

        try:
            return eval(expr, {"__builtins__": safe_builtins}, self.vars)
        except Exception as e:
            raise Exception(f"Can't eval '{expr}': {e}")

    def collect_expr(self, tokens, start):
        expr_tokens = []
        j = start
        paren_depth = 0
        while j < len(tokens):
            ttype, tval = tokens[j]

            if ttype == 'KEYWORD' and paren_depth == 0:
                break

            if tval == '(':
                paren_depth += 1
            elif tval == ')':
                paren_depth -= 1

            if ttype not in ('SKIP', 'NEWLINE', 'COMMENT'):
                expr_tokens.append(tval)

            j += 1
        return ' '.join(expr_tokens), j

    def parse_block(self, tokens, i):
        block = []
        if tokens[i][1] != '{':
            raise SyntaxError("Expected '{' to start a block")
        
        i += 1  # Skip the opening brace
        depth = 1
        while i < len(tokens):
            tok, val = tokens[i]
            if val == '{':
                depth += 1
            elif val == '}':
                depth -= 1
                if depth == 0:
                    i += 1
                    break
            if depth > 0:
                block.append(tokens[i])
            i += 1
        return block, i

    def run(self, tokens):
        i = 0
        while i < len(tokens):
            tok, val = tokens[i]

            if val == 'oi!':
                _, name = tokens[i+1]
                if tokens[i+2][0] != 'ASSIGN':
                    raise SyntaxError("Expected 'is' after variable name")
                expr, j = self.collect_expr(tokens, i + 3)
                if not expr.strip():
                    raise Exception(f"No expression provided for variable '{name}'")
                self.vars[name] = self.eval_expr(expr)
                i = j

            elif val == 'bawe':
                expr, j = self.collect_expr(tokens, i + 1)
                print(self.eval_expr(expr))
                i = j

            elif val == 'check mar':
                cond_tokens = []
                j = i + 1
                while j < len(tokens) and tokens[j][1] != '{':
                    cond_tokens.append(tokens[j][1])
                    j += 1

                if j >= len(tokens) or tokens[j][0] != 'LBRACE':
                    raise SyntaxError(f"Expected '{{' to start block, got: {tokens[j]}")

                cond = ' '.join(cond_tokens)
                block, j = self.parse_block(tokens, j)

                # Run block if main 'check mar' condition is true
                if self.eval_expr(cond):
                    self.run(block)
                    # Skip all following 'varna' blocks
                    while j < len(tokens) and tokens[j][1] == 'varna':
                        # Skip varna and its block
                        j += 1
                        depth = 0
                        while j < len(tokens):
                            if tokens[j][0] == 'LBRACE':
                                depth += 1
                            elif tokens[j][0] == 'RBRACE':
                                depth -= 1
                                if depth == 0:
                                    j += 1
                                    break
                            j += 1
                else:
                    matched = False
                    while j < len(tokens) and tokens[j][1] == 'varna':
                        j += 1
                        cond_tokens = []
                        while j < len(tokens) and tokens[j][0] != 'LBRACE':
                            cond_tokens.append(tokens[j][1])
                            j += 1

                        if j >= len(tokens) or tokens[j][0] != 'LBRACE':
                            raise SyntaxError("Expected '{' to start a block after varna")

                        cond_str = ' '.join(cond_tokens).strip()
                        block, j = self.parse_block(tokens, j)

                        # If it's just varna {, treat as else/default
                        if not cond_str or self.eval_expr(cond_str):
                            self.run(block)
                            matched = True
                            break
                    # If none matched, move on
                i = j


            elif val == 'edge till':
                cond_tokens = []
                j = i + 1
                while j < len(tokens) and tokens[j][1] != '{':
                    cond_tokens.append(tokens[j][1])
                    j += 1

                if j >= len(tokens) or tokens[j][0] != 'LBRACE':
                    raise SyntaxError(f"Expected '{{' to start block, got: {tokens[j]}")

                cond = ' '.join(cond_tokens)
                block, j = self.parse_block(tokens, j)
                while self.eval_expr(cond):
                    self.run(block)
                i = j

            elif val == 'goon':
                var_name = tokens[i+1][1]
                start = int(tokens[i+3][1])
                end = int(tokens[i+5][1])
                block, j = self.parse_block(tokens, i+6)
                for x in range(start, end):
                    self.vars[var_name] = x
                    self.run(block)
                i = j

            elif val == 'bawe aisa kar ki':
                func_name = tokens[i+1][1]
                if tokens[i+2][1] != '(':
                    raise SyntaxError("Expected '(' after function name")
                params = []
                j = i + 3
                while tokens[j][1] != ')':
                    if tokens[j][0] == 'IDENT':
                        params.append(tokens[j][1])
                    j += 1
                block, j = self.parse_block(tokens, j + 1)
                self.functions[func_name] = (params, block)
                i = j

            elif val == 'bawe ye kar':
                func_name = tokens[i+1][1]
                if tokens[i+2][1] != '(':
                    raise SyntaxError("Expected '(' in function call")
                args = []
                j = i + 3
                while tokens[j][1] != ')':
                    if tokens[j][0] not in ['SKIP', 'NEWLINE', 'RPAREN', 'LPAREN', 'COMMA']:
                        args.append(tokens[j][1])
                    j += 1
                evaluated_args = [self.eval_expr(arg) for arg in args]
                params, block = self.functions[func_name]
                if len(params) != len(evaluated_args):
                    raise ValueError("Argument count mismatch")
                old_vars = self.vars.copy()
                self.vars.update(dict(zip(params, evaluated_args)))
                self.run(block)
                self.vars = old_vars
                i = j + 1
                if self.returning is not None:
                    ret = self.returning
                    self.returning = None
                    self.vars[func_name] = ret

            elif val == 'wapas la dalle':
                expr, j = self.collect_expr(tokens, i + 1)
                self.returning = self.eval_expr(expr)
                return

            else:
                i += 1

# Entry point
if len(sys.argv) != 2:
    print("Usage: brainrot <filename>.rot")
    sys.exit(1)

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    code = f.read()

tokens = tokenize(code)

interp = Interpreter()
interp.run(tokens)