def print_head(n):
    if n == 0:
        return
    print_head( n - 1 )
    print(n)

print_head(3)