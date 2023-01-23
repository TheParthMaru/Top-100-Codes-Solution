## Even or odd

**Problem statement**

- Take an integer input and check whether it is an even number or odd number.

**Test cases**

```
Input: 26
Output: Even

Input: 11
Output: Odd

Input: 0
Output: Even
```

**Code**

*Approach 1: if-else*

```py
num = int(input())

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

*Approach 2: Ternary operator*

```py
num = int(input())

print("Even" if num % 2 == 0 else "Odd")
```

*Approach 3: Bitwise operator*

```py
num = int(input())

if num&1:
    print("Odd")
else:
    print("Even")
```