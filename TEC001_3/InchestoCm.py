while True:
    num = float(input("Enter Inches: "))
    if num > 0:
        numm = num*2.54
        print(f"{num} Inch(es) = {numm} Centimet(s)")
    else:
        break