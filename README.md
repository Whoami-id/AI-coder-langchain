# 🛠️ Auto Code and Test Generator with LangChain + OpenAI

This is a simple Python CLI tool that **auto-generates Python functions and their matching test cases** based on a task description you provide.

It uses:
- [LangChain](https://python.langchain.com/)
- [OpenAI API](https://platform.openai.com/)
- Python built-ins like `argparse`
- `.env` file for secure API key loading

---

## 📦 Features

- ✅ Generates clean, short Python functions
- ✅ Instantly creates test functions to verify behavior
- ✅ Modular design using LangChain's Pipe Operator (`|`)
- ✅ CLI interface to pass your own task and language
- ✅ Works with any OpenAI-compatible LLM

---

## 🚀 How to Use

### 1. Install dependencies

```bash
pip install langchain-openai python-dotenv
```

### 2. Set up your `.env` file

Create a `.env` file and add your OpenAI API key:

```bash
OPENAI_API_KEY=your-openai-api-key-here
```

### 3. Run the script

Basic usage:

```bash
python main.py
```

Custom task and language:

```bash
python main.py --task "sort a list of integers" --language "python"
```

Example output:

```plaintext
>>>>>> GENERATED CODE:
def sort_numbers(numbers):
    return sorted(numbers)

>>>>>> GENERATED TEST:
def test_sort_numbers():
    assert sort_numbers([3, 1, 2]) == [1, 2, 3]
```

---

## 🛠 Code Structure

| File          | Purpose                                |
|---------------|----------------------------------------|
| `main.py`     | The main Python script                 |
| `.env`        | Stores API key                         |
| `README.md`   | Project documentation                  |

---


