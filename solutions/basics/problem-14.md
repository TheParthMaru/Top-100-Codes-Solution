## Fibonacco series upto nth term

**Problem Statement**

- Take an input integer n and print the fibonacci series upto n.

**Test cases**

```
Input: 5
Output: 0 1 1 2 3 

Input: 10
Output: 0 1 1 2 3 5 8 13 21 34
```

**Code**

*Approach 1: Bruteforce*

```py
n = int(input())
termA = 0
termB = 1
print(f"{termA} {termB}", end=" ")

for i in range(3, n+1):
    next_term = termA + termB
    print(next_term, end=" ")

    termA = termB
    termB = next_term
```

*Approach 2: Recursive approach*
- Will do after studying recursion.