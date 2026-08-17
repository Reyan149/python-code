# ODD HUNT
#Topics: XOR Identity | XOR Cancellation | One Odd Occuring | XOR of Two | Split by Set Bit

a, b = 7,77

# Part 1: XOR Indentity and Equality
print('=== Odd Hunt ===')
print('a ^ a =', a ^ a )
print('a ^ 0 =', a ^ 0)
print('Equal (XOR):', (a ^ b) == 0)
print()

#Part 2": XOR Cancellation"
arr = [3, 5, 3, 5, 9]
result = 0
for n in arr: result ^= n
print('XOR of',arr, '=', result)
print()

#Part 3: One Odd-Occuring Number
nums = [4, 7, 4, 2, 7, 2, 9]
res = 0
for n in nums: res ^= n
print('Odd occuring:', res)
print()

#Part 4: XOR of Two Odd-Occuring Numbers
pair = [3, 9, 3, 5, 5, 7]
xab = 0
for n in pair: xab ^= n
print('XOR of two odds:', xab, '-->0, bin(xab))')
print()

# Part 5: Split by Rightmost Set Bit
setbit = xab & -xab
x, y = 0, 0
for n in pair:
    if n in pair:
        if n & setbit: x ^= n
        else: y ^= n
print('Two odd-occuring:', x, 'add', y)