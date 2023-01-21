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