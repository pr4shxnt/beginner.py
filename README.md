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
 
 # Extend the README.md with string methods/functions section

string_methods_section = """\

---

## 🔡 String Methods and Functions

Python provides many built-in methods for manipulating strings. Strings are immutable, so most methods return a new string.

### Common String Methods:

| Method                | Description                                 | Example                                 |
|-----------------------|---------------------------------------------|-----------------------------------------|
| `str.lower()`         | Converts all characters to lowercase        | `"HELLO".lower()` → `"hello"`          |
| `str.upper()`         | Converts all characters to uppercase        | `"hello".upper()` → `"HELLO"`          |
| `str.strip()`         | Removes leading/trailing whitespace         | `"  hello  ".strip()` → `"hello"`      |
| `str.replace(a, b)`   | Replaces substring `a` with `b`             | `"Hello".replace("H", "J")` → `"Jello"`|
| `str.find(sub)`       | Returns index of first occurrence of `sub` | `"hello".find("e")` → `1`              |
| `str.count(sub)`      | Counts number of times `sub` appears        | `"hello".count("l")` → `2`             |
| `str.startswith()`    | Checks if string starts with given value    | `"hello".startswith("he")` → `True`    |
| `str.endswith()`      | Checks if string ends with given value      | `"hello".endswith("lo")` → `True`      |
| `str.split(sep)`      | Splits string into a list by `sep`         | `"a,b,c".split(",")` → `["a", "b", "c"]`|
| `str.join(list)`      | Joins elements of list into a string        | `",".join(["a", "b", "c"])` → `"a,b,c"` |

### String Formatting:

```python
name = "Alice"
age = 25

# f-string
print(f"My name is {name} and I'm {age} years old.")

# .format() method
print("My name is {} and I'm {} years old.".format(name, age))
