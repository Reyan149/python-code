array = [1, 0, 7, 12, 0, 0, 9]
no_zero = []
for i in array:
    if i != 0:
        no_zero.append(i)

total_len = len(array)
no_zero_len = len(no_zero)
for i in range(total_len - no_zero_len):
    no_zero.append(0)
print(no_zero)