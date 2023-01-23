## Armstrong number

**Problem Statement**

- Take an integer number as input and check if it is armstrong or not.

**Test Cases**

```
Input: 153
Output: Armstrong

Input: 1634
Output: Armstrong

Input: 72
Output: Not an armstrong
```

**Code*

*Approach 1: Bruteforce approach*

```py
# Function to check armstrong
def is_armstrong(num):
    digits = count_digits(num)

    result = check_armstrong(num, digits)

    return result

# Function to count the number of digits
def count_digits(num):
    count = 0

    while(num != 0):
        count += 1
        num //= 10

    return count

# Function to calculate armstrong
def check_armstrong(num, digits):
    temp = num
    sum = 0
    while(temp != 0):
        last_digit = temp % 10
        sum = sum + pow(last_digit, digits)
        temp //= 10

    if sum == num:
        return True
    return False


# Main function
num = int(input())

if is_armstrong(num):
    print("Armstrong")
else:
    print("Not an armstrong")
```

*Approach 2: Recursive approach*
- Will do after studying recursion.