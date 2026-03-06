numbers = []
while True:
    num = input("Enter a series of numbers one by one(Press Enter to exist): ")
    if num!= '':
        try:
            nums = int(num)
            numbers.append(nums)
        except ValueError:
            print("Please Enter a number")
    else:
        break
numbers.sort(reverse=True)
print(numbers[:5])