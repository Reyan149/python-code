def ways(stairs):
    if stairs < 0:
        return 0
    elif stairs == 0:
        return 1
    return ways(stairs - 1) + ways(stairs - 2)

input('ways counts every distinct path up n stairs - 1 step or 2 steps at a time. Press Enter.')
print(" ways(3) =", ways(3))
print(" ways(4) =", ways(4))

n = int(input('Enter number of steps: '))
guess = input('What is ways(' + str(n) + ')? ') 
input('ways(stairs) = ways(stairs - 1) + ways(stairs - 2) bpth branches always combine. Press Enter.')
print(" ways(" + str(n) + ") =", ways(n), " your guess:", guess)