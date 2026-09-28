def tail_recur(n):
    if n == 0:
        return
    print(n)
    tail_recur(n - 1)

tail_recur(3)