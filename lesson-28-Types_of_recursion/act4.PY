def bounce(n):
    if n == 0:
        return[0]

    return [n] + bounce(n - 1) + [n]

print(bounce(3))
    