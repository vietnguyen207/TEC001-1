names = set()
while True:
    name = input("Enter a name or enter to quit: ")
    if name == '':
        break
    elif name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)
for i in names:
    print(i)