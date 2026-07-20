number = int(input('Enternumber to check : '))

og_num = number
reversed_num = 0

while number > 0:
    digit = number % 10
    reversed_num = reversed_num * 10 + digit
    number //= 10

if og_num == reversed_num:
    print(f'{og_num} is a Palindrome')
else:
    print(f'{og_num} is not a Palindrome')