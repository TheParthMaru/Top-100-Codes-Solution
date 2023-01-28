## Perfect number

**Problem statement**

- Take an integer input and check whether it is a perfect number or not.
- Eg of perfect number: 28 where sum of factors of 28 (1, 2, 4, 7, 14) is 28.

**Test cases**

```
Input: 28
Output: True

Input: 26
Output: False
```

**Code**

*Approach 1: Bruteforce approach*

```py
# Function to calculate strong number
num = int(input())
sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print(True)
else:
    print(False)
```

*Approach 2: Improved bruteforce approach*

```py
num = int(input())
sum = 0

for i in range(1, num//2 + 1):
    if num % i == 0:
        sum += i

if sum == num:
    print(True)
else:
    print(False)
```

*Approach 3: Recursive approach*

- Will do after studying recursion.