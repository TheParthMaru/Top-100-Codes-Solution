# Top-100-Codes-Solution
Top 100 codes of prep insta

**Palindrome Number**

_**Brute force approach**_
```py
def find_reverse(num):
    reverse = 0

    while(num != 0):
        last_digit = num % 10
        reverse = reverse * 10 + last_digit
        num //= 10

    return reverse

num = int(input())
reverse_num = find_reverse(num)

print(reverse_num)

if num == reverse_num:
    print("Palindrome")
else:
    print("Not a palindrome")
```

Other approaches: String slicing, recursion

**Armstrong number**
**_Iterative approach_**
```py
def check_armstrong(num):
    digits = count_digits(num)
    sum = 0
    temp = num
    while temp != 0:
       last_digit = temp % 10
       sum = sum + pow(last_digit, digits)
       temp //= 10

    if num == sum:
        return True
    else:
        return False

def count_digits(num):
    total_digits = 0
    while(num != 0):
        total_digits += 1
        num //= 10

    return total_digits

num = int(input())

if check_armstrong(num):
    print("Armstrong")
else:
    print("Not an armstrong")
```

**_Recursive approach_**