## Abundant number

**Problem statement**

- Take an integer input and check whether it is an abundant number or not.
- A Number that is smaller than the sum of all it's factors except the number itself is known as an Abundant number. 

**Explanation**

- Consider number = 12
- Factors of 12: 1, 2, 3, 4, 6 (Exclude the number itself)
- Sum of factors = 16
- If sum > number, then it is an abundant number.

**Test cases**

```
Input: 12
Output: True

Input: 10
Output: False
```

**Code**

*Approach 1: Bruteforce approach*

```py
num = int(input())
sum = 0

for i in range(1, (num // 2) + 1):
    if num % i == 0:
        sum += i

if sum > num:
    print(True)
else:
    print(False)
```