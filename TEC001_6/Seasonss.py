season = ("spring",'summer','autumn','winter')
while True:
    seasons = input('Enter a number of a month: ')
    try:
        seas = int(seasons)
        if seas == 12 or seas == 1 or seas == 2:
            print('This month is', season[3])
            break
        elif seas == 3 or seas ==4 or seas ==5:
            print('This month is', season[0])
            break
        elif seas == 6 or seas ==7 or seas ==8:
            print('This month is', season[1])
            break
        elif seas == 9 or seas ==10 or seas ==11:
            print('This month is', season[2])
            break
        else:
            print("Please enter a valid number")
    except:
        print("Please enter a number of a month")
