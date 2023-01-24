## Factorial of a number

**Problem statement**

- Take an integer input and calculate its factorial.

**Test cases**

```
Input: 5
Output: 120

Input: 0
Output: 1
```

**Code**

*Approach 1: Bruteforce*

```py
num = int(input())
fact = 1

for i in range(1, num+1):
    fact *= i

print(fact)
```

*Approach 2: Recursive*

- Will do after studying recursion.