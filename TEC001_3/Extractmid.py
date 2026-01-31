def extractmid():
    while True:
        string= input("Enter a random string: ") 
        strn = len(string)
        if strn % 2 == 0:
            strng = int(strn/2)
            print(string[strng-1:strng+1])
            break
        else:
            strng = int(strn/2)
            print(string[strng])
            break
extractmid()






