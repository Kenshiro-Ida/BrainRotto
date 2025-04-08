# BrainRot Language Interpreter

BrainRot is a fun, emoji and desi-language flavored interpreted language designed for creativity and chaos. This interpreter allows you to tokenize and execute `.rot` files written in BrainRot syntax.

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

## ▶️ How to Run

1. Save your BrainRot code in a file with the `.rot` extension.
2. Run the interpreter using Python:

```bash
python brainrot_interpreter.py your_code.rot
```

Replace `your_code.rot` with your actual filename.

---

## 🛠️ How to Make an EXE (Windows)

You can turn the interpreter into a standalone `.exe` using `pyinstaller`:

1. Install pyinstaller (if you haven't):
```bash
pip install pyinstaller
```

2. Run the following command to generate an executable:
```bash
pyinstaller --onefile brainrot_interpreter.py
```

3. After it's done, check the `dist` folder for `brainrot_interpreter.exe`.

Now you can run `.rot` files without needing Python installed!

```bash
brainrot_interpreter.exe your_code.rot
```

Make sure your `.rot` files are UTF-8 encoded and accessible from the same directory.
