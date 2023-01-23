## Prime number within a range

**Problem Statement**

- Take two integer inputs num1 and num2 and print all the prime numbers between num1 and num2 inclusive.

**Test Cases**

```
Input: 1 10
Output: 2 3 5 7

Input: 11 30
Output: 11 13 17 19 23 29

Input: 1 100
Output: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
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

num1 = int(input())
num2 = int(input())

for num in range(num1, num2+1):
    if is_prime(num):
        print(num, end = " ")
```