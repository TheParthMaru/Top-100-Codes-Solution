## Positive or negative number

**Problem Statement**
- Take an integer number as input and check whether it is positive, negative or zero.

**Test Cases**

```
Input: 5
Output: Positive

Input: -69
Output: Negative

Input: 0
Output: Zero
```

**Code**

*Approach 1: Bruteforce approach*

```py
num = int(input())

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

*Approach 2: Nested if-else*

```py
num = int(input())

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive")
else:
    print("Negative")
```

*Approach 3: Ternary operator*

```py
num = int(input())

print("Zero" if num == 0 else ("Positive" if num > 0 else "Negative"))
```