n = int(input("Enter a number: "))
num = n
rev = 0
while(n>0):
    dig = n % 10
    rev = rev * 10 + dig%10
    n = n//10
if(num == rev):
    print(f"{num} is a palindrome number.")
else:
    print(f"{num} is not a palindrome number.")