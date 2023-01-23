## Sum of n natural numbers

**Problem statement**

- Take an integer input n and calculate the sum of all the naturals upto n.

**Test cases**

```
Input: 10
Ouptut: 55

Input: 5
Ouptut: 15
```

**Code**

*Approach 1: for loop*

```py
n = int(input())
sum = 0

for i in range(1, n+1):
    sum += i

print(sum)
```

*Approach 2: Formula approach*

```py
n = int(input())

sum = (n * (n + 1)) // 2

print(sum)
```

*Approach 3: Recursive approach*

- Will do after learning recursion.