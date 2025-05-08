# Python Basics: Introduction, Modules, Variables, and Data Types

Welcome to this beginner-friendly guide to Python programming! This README provides a foundational overview of key Python concepts.

---

## 📌 Introduction to Python

**Python** is a high-level, interpreted, general-purpose programming language. It is known for its simplicity, readability, and broad community support.

### Features of Python:
- Easy to learn and write
- Interpreted and dynamically typed
- Extensive standard library
- Cross-platform
- Open-source

### Hello World in Python:
```python
print("Hello, World!")
```

---

## 📦 Modules in Python

A **module** is a file containing Python definitions and functions. Modules help organize code into manageable parts.

### Importing a Module:
```python
import math

print(math.sqrt(25))  # Outputs: 5.0
```

### Custom Module:
Create a file `mymodule.py`:
```python
def greet(name):
    return f"Hello, {name}!"
```

Use it in another file:
```python
import mymodule

print(mymodule.greet("Alice"))
```

---

## 📝 Variables in Python

A **variable** is a name that references a value. Python variables are created when you assign a value.

### Example:
```python
x = 10
name = "John"
is_active = True
```

- Python is **dynamically typed** – you don’t need to declare the type.

### Variable Naming Rules:
- Must start with a letter or underscore
- Can contain letters, numbers, underscores
- Case-sensitive (`age` ≠ `Age`)

---

## 🔢 Data Types in Python

Python has several built-in data types categorized as follows:

### Basic Data Types:
| Type      | Example        |
|-----------|----------------|
| `int`     | `10`           |
| `float`   | `3.14`         |
| `str`     | `"Hello"`      |
| `bool`    | `True`, `False`|

### Collection Data Types:
| Type       | Description                     | Example                      |
|------------|---------------------------------|------------------------------|
| `list`     | Ordered, mutable sequence       | `[1, 2, 3]`                  |
| `tuple`    | Ordered, immutable sequence     | `(1, 2, 3)`                  |
| `set`      | Unordered, no duplicates        | `{1, 2, 3}`                  |
| `dict`     | Key-value pairs (hashmap)       | `{"name": "Alice", "age": 25}` |

### Type Checking:
```python
x = 10
print(type(x))  # <class 'int'>
```

---
 