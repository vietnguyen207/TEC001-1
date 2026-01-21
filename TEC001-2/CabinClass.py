def cabinclass():
    while True:
        cabin = input("Enter your cabin class: ")
        if cabin.upper() == "LUX":
            print("Your cabin is upper-deck cabin with a balcony.")
            break
        elif cabin.upper() == "A":
            print("Your cabin is above the car deck, equipped with a window.")
            break
        elif cabin.upper() == "B":
            print("Your cabin is windowless cabin above the car deck.")
            break
        elif cabin.upper() == "C":
            print("Your cabin is windowless cabin below the car deck.")
            break
        else:
            print("Invalid Cabin Class")
cabinclass()

        