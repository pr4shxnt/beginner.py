
# 🐍 Created with love by Prashant

This guide introduces **functions** in Python — a key concept for writing clean, reusable, and modular code.

---

## 📚 What is a Function?

A **function** is a block of reusable code that performs a specific task.

Instead of repeating code, you define it once and call it whenever needed.

---

## 🧱 Why Use Functions?

- Organize code better
- Avoid repetition (DRY principle)
- Improve readability and debugging
- Enable reuse and testing

---

## 🛠️ Defining a Function

### Basic Syntax

```python
def function_name():
    # code block
```

### Example

```python
def greet():
    print("Hello, world!")
```

To call the function:

```python
greet()
```

---

## 🧾 Functions with Parameters

### Example

```python
def greet(name):
    print("Hello,", name)

greet("Prashant")
greet("Prabesh")
```

You can pass multiple parameters:

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

---

## 🔁 Return Values

Functions can return data using the `return` keyword.

```python
def square(x):
    return x * x

print(square(4))  # Output: 16
```

---

## 📦 Default Parameters

You can provide default values for parameters:

```python
def greet(name="Guest"):
    print("Hello,", name)

greet()         # Output: Hello, Guest
greet("Prashant")  # Output: Hello, Prashant
```

---

## 🧮 Keyword Arguments

Call functions using named arguments:

```python
def intro(name, age):
    print(f"{name} is {age} years old.")

intro(age=25, name="Prabesh")
```

---

## 🎯 Arbitrary Arguments

Use `*args` and `**kwargs` for flexible inputs.

### `*args` – multiple positional arguments

```python
def total(*numbers):
    return sum(numbers)

print(total(1, 2, 3, 4))  # Output: 10
```

### `**kwargs` – multiple keyword arguments

```python
def display_info(**info):
    for key, value in info.items():
        print(key, ":", value)

display_info(name="Prashant", age=30)
```

---

## 🧠 Scope and Local Variables

Variables defined inside a function are **local**:

```python
def demo():
    x = 10  # local variable / block scoped
    print(x)

demo()
# print(x)  # Error: x is not defined outside
```

Use `global` if you must access a global variable:

```python
count = 0

def increment():
    global count
    count += 1
```

---

## 🔁 Recursion

A function calling itself:

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

Use with care — make sure there's a **base case** to stop.

---

## 📘 Lambda (Anonymous) Functions

Short, one-line functions:

```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

---

## ✅ Practice Examples

### 1. Function to find maximum of 3 numbers

```python
def maximum(a, b, c):
    return max(a, b, c)
```

### 2. Function to reverse a string

```python
def reverse_string(s):
    return s[::-1]
```

### 3. Function to check if number is even

```python
def is_even(n):
    return n % 2 == 0
```

---Created with love by Prashant