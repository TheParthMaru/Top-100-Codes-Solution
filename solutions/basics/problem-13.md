## Armstrong number between two intervals

**Problem Statement**

- Take two integer numbers as input and find all the armstrong numbers between this interval.

**Test cases**

```
Input: 1 10
Output: 1 2 3 4 5 6 7 8 9

Input: 10 500
Output: 153 370 371 407
```

**Code**

*Approach 1: Bruteforce approach*

```py
# Checks whether the number is armstrong or not
def is_armstrong(num):
    digits = count_digits(num)
    temp = num
    sum = 0

    while(temp != 0):
        last_digit = temp % 10
        sum = sum + pow(last_digit, digits)
        temp //= 10

    if sum == num:
        return True
    return False

# Count of the digits in the number
def count_digits(num):
    count = 0
    while(num != 0):
        count += 1
        num //= 10

    return count

# Main
num1 = int(input())
num2 = int(input())

for num in range(num1, num2+1):
    if is_armstrong(num):
        print(num, end = " ")
```