
# 🐍 Created with love by Prashant

This guide covers all the basics of **loops** and **iteration** in Python. It's designed to help beginners understand how to repeat code efficiently and work with different types of data.

---

## 📚 What is a Loop?

A **loop** is used to execute a block of code **repeatedly**. Python has two main types of loops:

1. `for` loops – loop over a sequence (like a list, string, or range)
2. `while` loops – repeat as long as a condition is `True`

---

## 🔁 `for` Loops

### Basic Syntax:

```python
for item in iterable:
    # code block
```

### Example: Loop over a list

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### Example: Loop over a string

```python
for letter in "Python":
    print(letter)
```

### Using `range()`:

```python
for i in range(5):
    print(i)  # prints 0 to 4
```

You can also specify start and step:

```python
for i in range(1, 10, 2):
    print(i)  # prints 1, 3, 5, 7, 9
```

---

## 🔄 `while` Loops

### Basic Syntax:

```python
while condition:
    # code block
```

### Example: Count from 1 to 5

```python
count = 1
while count <= 5:
    print(count)
    count += 1
```

⚠️ Make sure the condition eventually becomes `False`, or it becomes an **infinite loop**!

---

## ⛔ Loop Control Statements

### `break` – Exit the loop early

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### `continue` – Skip the current iteration

```python
for i in range(5):
    if i == 2:
        continue
    print(i)  # skips 2
```

### `pass` – Do nothing (placeholder)

```python
for i in range(3):
    pass  # often used when code is not ready yet
```

---

## 🌀 Nested Loops

You can place loops inside other loops.

```python
for i in range(2):
    for j in range(3):
        print(f"i={i}, j={j}")
```

---

## 🧠 Looping with `else`

Python allows an `else` block after loops.

```python
for i in range(3):
    print(i)
else:
    print("Loop finished!")
```

🔸 Note: If a `break` occurs, the `else` is skipped.

---

## 💡 Looping with `enumerate()` and `zip()`

### `enumerate()` – Get index and value

```python
names = ["Prashant", "Prabesh", "Sujan"]
for index, name in enumerate(names):
    print(index, name)
```

### `zip()` – Loop over multiple sequences

```python
names = ["Prashant", "Prabesh"]
scores = [85, 92]
for name, score in zip(names, scores):
    print(name, score)
```

---

## 🧮 Common Use Cases

- Iterating through lists, tuples, strings
- Repeating code a number of times
- Processing user input or sensor data
- Automating repetitive tasks
- Searching or filtering data

---

## 🎯 Practice Program

Check  ``` hangmanGame.py ``` 

or

Check ``` number_guess_game.py ```


### Creating a right angled triangle using for loop

```python

i = 0

for i in range(10):
    print("*"*i) 


```
---

