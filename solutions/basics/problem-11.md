## Palindrome number

**Problem Statement**

- Take an integer number as input and check if it is palindrome or not.
- Palindrome number is a number when reversed will be same as the original.

**Test Cases**

```
Input: 12321
Output: Palindrome

Input: 1221
Output: Palindrome

Input: 567
Output: Not a palindrome
```

**Code*

*Approach 1: Bruteforce approach*

```py
# Function to check palindrome
def is_palindrome(num):
    reverse = get_reverse(num)

    if reverse == num:
        return True
    return False

# Function to reverse the number
def get_reverse(num):
    reverse_num = 0
    temp = num
    while(temp != 0):
        last_digit = temp % 10
        reverse_num = reverse_num * 10 + last_digit
        temp //= 10
    
    return reverse_num

# Main
num = int(input())

if is_palindrome(num):
    print("Palindrome")
else:
    print("Not a palindrome")
```

*Approach 2: Recursive approach*
- Will do after studying recursion.