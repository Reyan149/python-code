def flip_name(s):
    if len(s) == 1:
        return s
    return flip_name(s[1:]) + s[0]

input('flip_name recurses on s[1:] then attaches s[0] at the end. Press Enter.')
print('flip_name("Maya") =', flip_name("Maya"))
print('flip_name("Python") =', flip_name("Python"))

name = input('Enter a name (try "Alice" or "Bob"): ')
guess = input('What is flip_name("' + name + '")? ')
print('flip_name("' + name + '") =', flip_name(name), ' your guess:', guess)