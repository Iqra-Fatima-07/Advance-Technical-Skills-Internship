def print_N_to_1(n):
    if n < 1:
        return
    print(n, end=" ")
    print_N_to_1(n - 1)

print_N_to_1(5)
