def reverse_number(n, temp=0):
    if n == 0:
        return temp
    return reverse_number(n // 10, temp * 10 + n % 10)

print(reverse_number(1234))
