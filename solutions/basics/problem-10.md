## Reverse of a number

**Problem Statement**

- Take an integer number as input and reverse it.

Note: Ignore leading and trailing 0s.

**Test Cases**

```
Input: 12345
Output: 54321

Input: 5697
Output: 7965

Input: 10000
Output: 1

Input: 100001
Output: 100001
```

**Code**

*Approach 1: Bruteforce approach*

```py
def reverse_num(num):
    reverse = 0
    temp = num

    while(temp != 0):
        last_digit = temp % 10
        reverse = reverse * 10 + last_digit
        temp //= 10
    
    return reverse

num = int(input())

print(reverse_num(num))
```

*Approach 2: String slicing approach*
- Will do after studying strings.

*Approach 3: Recursive approach*
- Will do after studying recursion.