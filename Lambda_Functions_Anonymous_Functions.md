# Lambda Functions (Anonymous Functions)

## Syntax 
```python
lambda arguments: expression
```

## [+] Example
```python
square = lambda x: x ** 2
print(square(5))  # 25

## Equivalent to:

def square(x):
    return x ** 2
```

## <code>map()</code> – Apply a function to each item

```python
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
print(squared)  # [1, 4, 9, 16]
```

## <code>filter()</code> – Keep only items that meet a condition

```python
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # [2, 4]
```

## <code>reduce()</code> – Combine all items into one result

```python

from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # 24

```