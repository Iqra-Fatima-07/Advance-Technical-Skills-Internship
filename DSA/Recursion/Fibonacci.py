def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def print_fibonacci_series(terms):
    if terms <= 0:
        print("Please enter a positive integer.")
        return
    for i in range(terms):
        print(fibonacci(i), end=" ")


print_fibonacci_series(7)
