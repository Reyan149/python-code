input('XOR swap - exchange two values withouta third variable. Press Enter')
print(' berore: a = 5   b = 9')
a, b = 5, 9
a ^= b; b ^= a; a ^= b
print(' after: a =', a, 'b =', b)

n = int(input('Enter a number (try 3 or 7): '))
guess = input('After XOR swap of ' + str(n) + ', and 8 what is the value of n? ')
a, b = n, 8
a ^= b; b ^= a; a ^= b
input('XOR swap exchanges the values of a and b. Press Enter to see the answer.')
print('The value of n after XOR swap is', a, 'you guessed', guess)
