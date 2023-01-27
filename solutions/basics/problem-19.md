## Strong number

**Problem statement**

- Take an integer input and check whether it is a strong number or not.
- Eg of strong number: 145 = 1! + 4! + 5!

**Test cases**

```
Input: 145
Output: True

Input: 153
Output: False
```

**Code**

*Approach 1: Iterative approach*

```py
# Function to calculate strong number
def is_strong_number(num):
    sum = 0
    temp = num

    while(temp != 0):
        last_digit = temp % 10
        sum += factorial(last_digit)
        temp //= 10

    if sum == num:
        return True

    return False

# Function to calculate factorial
def factorial(num):
    fact = 1

    for i in range(1, num+1):
        fact *= i

    return fact

# Main
num = int(input())
print(is_strong_number(num))
```

*Approach 2: Recursive approach*

- Will do after studying recursion.