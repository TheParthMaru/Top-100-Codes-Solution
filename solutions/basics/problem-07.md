## Prime number

**Problem Statement**

- Take an integer input num as check whether it is prime or not.

**Test Cases**

```
Input: 5
Output: Prime

Input: 8
Output: Composite

Input: 1
Output: Composite

Input: -5
Output: Composite
```

**Code**

*Approach 1: Bruteforce approach*

```py
import math

def is_prime(num):
    if num <= 1:
        return False

    for divisor in range(2, int(math.sqrt(num) + 1)):
        if num % divisor == 0:
            return False
            
    return True


num = int(input())
if is_prime(num):
    print("Prime")
else:
    print("Composite")
```

*Approach 2: For large input values, skip common iterations*

```py
import math

def is_prime(num):
    if num <= 1:
        return False

    if num == 2 or num == 3:
        return True
    
    if num % 2 == 0 or num % 3 == 0:
        return False

    for divisor in range(5, int(math.sqrt(num) + 1), 6):
        if (num % divisor == 0) or (num % (divisor + 2) == 0):
            return False

    return True


num = int(input())
if is_prime(num):
    print("Prime")
else:
    print("Composite")
```