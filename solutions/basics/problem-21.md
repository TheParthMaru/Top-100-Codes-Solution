## Perfect square

**Problem statement**

- Take an integer input and check whether it is a perfect square or not.

**Test cases**

```
Input: 100
Output: True

Input: 25
Output: True

Input: 61
Output: False
```

**Code**

*Approach 1: Bruteforce approach*

```py
import math

num = int(input())

if math.floor(math.sqrt(num)) == math.ceil(math.sqrt(num)):
    print(True)
else:
    print(False)
```