numb = int(input("Enter a integer number to check if it is a prime number: "))
if numb % 2 == 0:
    print("Not a prime Number")
elif numb % 3 == 0:
    print("Not a prime Number")
elif numb % 5 == 0:
    print("Not a prime Number")
else:
    print("It's a prime number")