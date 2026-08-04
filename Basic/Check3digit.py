#check 3 digit number
n = int(input("Enter a number: "))
if n >= 100 and n <= 999:
    print(f"{n} is a 3-digit number.")
else:   
    print(f"{n} is not a 3-digit number.")
