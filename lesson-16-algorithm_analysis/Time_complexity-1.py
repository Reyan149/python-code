n =4
print('Counting Game Points (m=', n, 'rounds)')
print()

total = n *(n + 1) // 2
print('Formula way : total =', total,'| steps - 1')

total = 0
steps = 0
for round_num in range(1, n + 1):
    total += round_num
    steps += 1
print('Loop way : total =', total,'| steps -', steps)

total = 0
steps = 0
nested_steps = 0
for round_num in range(1, n + 1):
    for point in range(1, round_num + 1):
        nested_steps += 1

n = 10
nested_steps = 0
for round_num in range(1, n + 1):
    for point in range(1, round_num + 1):
        nested_steps += 1

print()
print('Now with n =', n, 'rounds')
print('Formula way : steps =  (always 1)')
print('Loop way : steps =', n)
print('Nested loop way : steps =', nested_steps, '(grows faster)')
print()
print('Same answer - but very different cost. Thats time complexity!')
