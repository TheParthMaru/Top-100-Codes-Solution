## HCF/ GCD

**Problem statement**

- Take two integer inputs and find its gcd.

**Test cases**

```
Input: 9 81
Output: 9

Input: 5 7
Output: 1
```

**Code**

*Approach 1: Bruteforce approach*

```py
num1 = int(input())
num2 = int(input())

gcd = 1

for i in range(2, min(num1, num2) + 1):
    if (num1 % i ==  0) and (num2 % i ==  0):
        gcd = i

print(gcd)
```

*Approach 2: Repetitive subtraction approach*

```py
num1 = int(input())
num2 = int(input())

while(num1 != num2):
    if num1 > num2:
        num1 = num1 - num2
    else:
        num2 = num2 - num1

print(num1)
```

*Approach 3: Recursion based approach*
- Will be solved after learning recursion.