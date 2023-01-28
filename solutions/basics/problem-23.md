## Harshad number

**Problem statement**

- Take an integer input and check whether it is an automorphic number or not.
- For eg, consider 21, sum of digits of 21 = 3 and 21 is divisible by 3 so 21 is Harshad number.

**Test cases**

```
Input: 21
Output: True

Input: 81
Output: True

Input: 25
Output: False
```

**Code**

*Approach 1: Bruteforce approach*

```py
def calculate_sum_of_digits(num):
    sum = 0
    while(num != 0):
        last_digit = num % 10
        sum += last_digit
        num //= 10
    return sum

num = int(input())
sum_of_digits = calculate_sum_of_digits(num)

if num % sum_of_digits == 0:
    print(True)
else:
    print(False)
```