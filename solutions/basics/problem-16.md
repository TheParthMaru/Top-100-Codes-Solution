## Power of a number

**Problem statement**

- Take two integer inputs x and n and calculate x to the power of n.

**Test cases**

```
Input: 2 3
Output: 8

Input: 8 0
Output: 1
```

**Code**

*Approach 1: Iterative approach*

```py
x = int(input())
n = int(input())
result = 1

while n >= 1:
    result *= x
    n -= 1

print(result)
```

*Approach 2: Exponentiation Operator*

```py
x = int(input())
n = int(input())

print(x ** n)
```

*Approach 3: `pow()`*

```py
x = int(input())
n = int(input())

print(pow(x, n))
```
