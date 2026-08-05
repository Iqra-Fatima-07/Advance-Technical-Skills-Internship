def sum_of_N(n):
    if n <= 1:
        return n
    return n + sum_of_N(n - 1)

print(sum_of_N(5))
