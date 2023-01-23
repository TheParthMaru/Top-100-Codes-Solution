## Greatest of three numbers

**Problem statement**

- Take three integer inputs num1, num2 and num3 on seperate lines and find which number is greatest among the three.

**Test Cases**

```
Input: 1 2 3
Output: 3

Input: -3 -1 -2
Output: -1

Input: 69 69 69
Output: 69
```

**Code**

*Approach 1: if-else*

```py
num1 = int(input())
num2 = int(input())
num3 = int(input())

if (num1 >= num2) and (num1 >= num3):
    print(num1)
elif num2 >= num3:
    print(num2)
else:
    print(num3)
```

*Approach 2: Ternary operator*

```py
num1 = int(input())
num2 = int(input())
num3 = int(input())

print(num1 if (num1 >= num2) and (num1 >= num3) else (num2 if num2 >= num3 else num3))
```