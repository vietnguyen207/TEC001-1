def leapyear():
    while True:
        year = input("Enter a year to check if it is leap year: ")
        try:
            yearr= int(year)
        except:
            print("Invalid Input \nPlease Try Again")
        if yearr % 4 == 0 and yearr % 100 !=0:
            print("This year is a leap year!")
            break
        elif yearr % 100 == 0 and yearr % 400 == 0:
            print("This year is a leap year!")
            break
        else:
            print("This year is not a leap year")
            break
leapyear()