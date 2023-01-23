## Sum of digits of a number

**Problem Statement**

- Given an integer number, calculate the sum of all the digits of that number.

**Test Cases**

```
Input: 12345
Output: 15

Input: 100001
Output: 2
```

**Code**

*Approach 1: Bruteforce approach*

```py
num = int(input())
sum = 0

while num != 0:
    last_digit = num % 10
    sum += last_digit
    num //= 10

print(sum)
```

*Approach 2: Python trick*

```py
# Take input in li
li = [int(x) for x in input().split("")]
print(sum[li])
```

*Approach 3: Recursive approach*

- Will do after learning recursion.