#count even and odd numbers in a array
arr = [1,2,3,4,5,6,7,8,9,10, 11,12,13,14,15,16,17]
even_count = 0
odd_count = 0
for num in arr:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(f"Number of even numbers: {even_count}")
print(f"Number of odd numbers: {odd_count}")