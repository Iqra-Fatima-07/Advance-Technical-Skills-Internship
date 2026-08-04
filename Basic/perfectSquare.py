#perfect square
def is_perfect_square(n):
    if n < 0:
        return False
    root = int(n**0.5)
    return root * root == n

print(is_perfect_square(16))
print(is_perfect_square(15))
print(is_perfect_square(-16))