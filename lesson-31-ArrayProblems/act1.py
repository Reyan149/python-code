n = int(input('Enter a limit : '))
numbers = range(1, n+1)
print(numbers)

lst_numbers = list(numbers)
print(lst_numbers)

start = 0
end = n - 1

while start < end:
    lst_numbers[start], lst_numbers[end] = lst_numbers[end], lst_numbers[start]
    start += 1
    end -= 1

print('Reversed List:', lst_numbers)