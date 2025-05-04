# ✅ Python Comprehensions Cheat Sheet

Python comprehensions provide a concise way to create lists, sets, and dictionaries.

---

## 🔹 1. Basic List Comprehension

### Syntax:
```python
[expression for item in iterable]
```
## Square Example
```python
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

## List Comprehension with Condition
```python
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

## Nested List Comprehension
```python
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(table)  # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

## Flatten a List of Lists
```python
nested = [[1, 2], [3, 4], [5]]
flat = [num for sublist in nested for num in sublist]
print(flat)  # [1, 2, 3, 4, 5]
```

## Dictionary Comprehension
```python
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# with condition

even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

## Set Comprehension
```python
unique_lengths = {len(word) for word in ["hi", "hello", "world", "hi"]}
print(unique_lengths)  # {2, 5}
```
