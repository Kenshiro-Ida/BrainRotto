# BrainRotto Language Interpreter

BrainRotto is a fun, emoji and desi-language flavored interpreted language designed for creativity and chaos. This interpreter allows you to tokenize and execute `.rot` files written in BrainRot syntax.

## 🔥 Features

- Custom keywords like `oi!`, `check mar`, `varna`, `bawe`, `edge till`, etc.
- Emoji operators like `➕`, `➖`, `✖️`, `➗`, `🟰`, `❌`
- Built-in conditional (`check mar` / `varna`) and loops (`edge till`, `goon`)
- Function definitions (`bawe aisa kar ki`) and calls (`bawe ye kar`)
- Expression evaluation, input handling (`sun`), and return (`wapas la dalle`)
- Basic tokenization with custom lexer
- Safe evaluation environment

## 🚀 Usage

```bash
python brainrot_interpreter.py your_code.rot
```

## 📄 Example Code (.rot)

```rot
oi! x is 10
check mar x 🔼 5 {
    bawe "Greater than 5"
} varna {
    bawe "5 or less"
}
```

## 🧠 Syntax Highlights

| BrainRot          | Python Equivalent |
|-------------------|-------------------|
| `oi!`             | `let`             |
| `check mar`       | `if`              |
| `varna`           | `else`            |
| `edge till`       | `while`           |
| `goon x till y`   | `for x in range(x, y)` |
| `bawe aisa kar ki`| `def`             |
| `bawe ye kar`     | `function call`   |
| `wapas la dalle`  | `return`          |
| `sun`             | `input()`         |
| `yup` / `nah`     | `True` / `False`  |

## 💬 Notes

- This interpreter is written in pure Python and designed for educational, creative, and fun purposes.
- Use UTF-8 encoded `.rot` files for compatibility with emojis.

## 📁 License

MIT License
