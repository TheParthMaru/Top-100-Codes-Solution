## Automorphic num

**Problem statement**

- Take an integer input and check whether it is an automorphic number or not.
- For eg, consider 5, 5 * 5 = 25 whose last digit is 5, so its an automorphic number.
- For eg, consider 25, 25 * 25 = 625 whose last 2 digit contains 25, so its an automorphic number.

**Test cases**

```
Input: 5
Output: True

Input: 6
Output: True

Input: 25
Output: True

Input: 9
Output: False
```

**Code**

*Approach 1: Bruteforce approach*

```py
def count_digits(num):
    count = 0
    while(num != 0):
        count += 1
        num //= 10
    
    return count

n = int(input())
digits_of_n = count_digits(n)
square_of_n = n ** 2

temp = 0
place_value = 1
while(digits_of_n >= 1):
    last_digit = square_of_n % 10
    temp = last_digit * place_value + temp
    place_value *= 10
    digits_of_n -= 1
    square_of_n //= 10

if n == temp:
    print(True)
else:
    print(False)
```

*Approach 2: String based approach*
- Will do after learning strings concepts.