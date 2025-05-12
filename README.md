# Python Basics: Introduction, Modules, Variables, Data Types, Operations and String methods

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

print(mymodule.greet("Prashant"))
```

---

## 📝 Variables in Python

A **variable** is a name that references a value. Python variables are created when you assign a value.

### Example:
```python
x = 10
name = "Prashant"
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
| `dict`     | Key-value pairs (hashmap)       | `{"name": "Prashant", "age": 17}` |

### Type Checking:
```python
x = 10
print(type(x))  # <class 'int'>
```

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



# 📘 Python Operations, Operators, Slicing & Indexing

## 📌 Python Arithmetic Operations

Used for basic mathematical calculations:

```python
a = 10
b = 3

print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation
print(a // b) # Floor Division
```

---

## 📊 Comparison Operators

Used to compare two values:

```python
a = 5
b = 10

print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)   # Greater than
print(a < b)   # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to
```

---

## 🧠 Logical Operators

Used to combine conditional statements:

```python
x = True
y = False

print(x and y)  # Logical AND
print(x or y)   # Logical OR
print(not x)    # Logical NOT
```

---

## 🖋 Assignment Operators

Used to assign values to variables:

```python
a = 10
a += 5  # a = a + 5
a -= 3
a *= 2
a /= 4
a %= 2
a **= 3
a //= 2
```

---

## ⚙ Bitwise Operators

Work on bits and perform bit-by-bit operations:

```python
a = 5      # 0b0101
b = 3      # 0b0011

print(a & b)  # AND
print(a | b)  # OR
print(a ^ b)  # XOR
print(~a)     # NOT
print(a << 1) # Left shift
print(a >> 1) # Right shift
```

---

## 👁 Identity and Membership Operators

### Identity Operators:
```python
x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)  # True
print(x is z)  # False
print(x is not z)  # True
```

### Membership Operators:
```python
my_list = [1, 2, 3, 4]

print(2 in my_list)   # True
print(5 not in my_list) # True
```

---

## 🧱 Indexing in Python

Indexing gives you access to individual elements in a sequence (like strings, lists, tuples):

```python
my_list = [10, 20, 30, 40, 50]

print(my_list[0])  # 10
print(my_list[-1]) # 50
```

---

## ✂️ Slicing in Python

Slicing allows you to extract a portion of a list or string:

```python
my_list = [0, 1, 2, 3, 4, 5, 6]

print(my_list[1:5])   # [1, 2, 3, 4]
print(my_list[:3])    # [0, 1, 2]
print(my_list[3:])    # [3, 4, 5, 6]
print(my_list[::2])   # [0, 2, 4, 6]
print(my_list[::-1])  # [6, 5, 4, 3, 2, 1, 0] (reverse list)
```

---

## 🎯 Practice Program

Check  ``` phone_number_balance_handler.py ``` 



## ✅❌ Conditional Statements

"Conditional statements allow a program to execute certain blocks of code or functions only if specified conditions are met. For example, using ```if``` to run a function when a condition is true, and ```else``` to run a different function when it's false.

```python
a = "male"

if a == "male":
  print("You are a male!!")
else:
  print("You are a cute little girlie and feminine character.")

# returns "You are a male!!"

```

Lets say in some cases, 3 or 4 options apply for the code. For example; we got extra 1 extra gender ie. transgender and people could choose "rather not say". Here comes else if statement countering the first if statement returns negative boolean value. 
 ```python

a = "prefer not to say"

if a == "male": 
    print("You are a male!!")
elif a == "transgender":
    print("You are a transgender")
elif  a == "female":
    print("Just marry me already🌹🌹🌹")
else:
    print("You're cooked. You chose rather not to express your gender. Such a gay thing to do.")


#returns "You're cooked. You chose rather not to express your gender. Such a gay thing to do."

```


---