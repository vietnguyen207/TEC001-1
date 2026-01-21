def zanderlength():
    while True:
        zander = input("Enter the length of a zander(cm): ")
        try:
            z = float(zander)
            break
        except:
            print("Invalid input \n Please Try Again")
    if z < 42:
        size = 42 - z
        print(f"Please release the zander to the lake \nThe caught fish was {size} below the size limit \nThe fish must 42 centimets or longer!")
    else:
        print("The zander is valid")
zanderlength()