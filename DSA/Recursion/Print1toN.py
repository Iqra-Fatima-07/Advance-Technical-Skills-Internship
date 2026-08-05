def print_1_to_N(n):
    if n < 1:
        return
    print_1_to_N(n - 1)
    print(n, end=" ")



print_1_to_N(5)
