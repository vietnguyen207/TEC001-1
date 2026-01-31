numbers = []

while True:
    num = input("Enter a number (press Enter to quit): ")

    if num == "":
        break
        
    number = float(num)
    numbers.append(number)

if len(numbers) > 0:
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
else:
    print("No numbers were entered.")
