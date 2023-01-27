## Prime factors of a number

**Problem statement**

- Take an integer input and calculate all of its prime factors.

**Test cases**

```
Input: 10
Output: 2 5

Input: 5
Output: 5
```

**Code**

*Approach 1: Iterative approach*

```py
import math

def prime_factors(num):
    if is_prime(num):
        print(num)
        return

    for i in range(2, int(math.sqrt(num) + 1)):
        if (num % i == 0) and is_prime(i):
            print(i, end=" ")

def is_prime(num):
    for divisor in range(2, int(math.sqrt(num) + 1)):
        if num % divisor == 0:
            return False
    return True

num = int(input())
prime_factors(num)
```

