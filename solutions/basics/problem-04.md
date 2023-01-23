## Greatest of two numbers

**Problem statement**

- Take two integer inputs num1 and num2 on seperate lines and find which number is greatest among the two.

**Test cases**

```
Input: 5 6
Output: 6

Input: -2 -1
Output: -1

Input: 2 2
Output: Equal
```

**Code**

*Approach 1: if-else*

```py
num1 = int(input())
num2 = int(input())

if num1 > num2:
    print(num1)
elif num1 < num2:
    print(num2)
else:
    print("Equal")
```

*Approach 2: Ternary operator*

```py
num1 = int(input())
num2 = int(input())

print(num1 if num1 > num2 else(num2 if num1 < num2 else "Equal"))
```

*Approach 3: Built-in max() function*

```py
# Using max() won't allow you to print "Equal"
num1 = int(input())
num2 = int(input())

print(max(num1, num2))
```