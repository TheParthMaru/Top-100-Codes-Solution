## Factor of a number

**Problem statement**

- Take an integer input and calculate all of its factors.

**Test cases**

```
Input: 10
Output: 1 2 5 10

Input: 5
Output: 1 5
```

**Code**

*Approach 1: Iterative approach*

```py
num = int(input())

for i in range(1, num+1):
    if num % i == 0:
        print(i, end = " ")
```