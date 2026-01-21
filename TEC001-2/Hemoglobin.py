def hemoglobin():    
    while True:
        gender = input("What is your gender (Man/Woman): ")
        if not gender:
            print("Please Enter Your Gender!")
        elif gender.lower() == "man":
            break
        elif gender.lower() == "woman":
            break
        else:
            print("Invalid input\nPlease Try Again")
    if gender.lower() == "man":
        while True:
            hemomale = input("What is your hemoglobin value: ")
            try:
                hemom = float(hemomale)
            except:
                print("Invalid Input\nPlease Try Again")
            if 134<= hemom <=167:
                print("Your hemoglobin value is normal")
                break
            elif hemom<134:
                print("Your hemoglobin value is low")
                break
            elif 167<hemom<300:
                print("Your hemoglobin value is high")
                break
            else:
                print("Please Try Again")
    if gender.lower() == "woman":
        while True:    
            hemofemale = input("What is your hemoglobin value(g/l): ")
            try:
                hemof = float(hemofemale)
            except:
                print("Invalid Input")         
            if 117<= hemof <=155:
                print("Your hemoglobin value is normal")
                break
            elif hemof<117:
                print("Your hemoglobin value is low")
                break
            elif 155.0 < hemof < 300.0:
                print("Your hemoglobin value is high")
                break
            else:
                print("Please Try Again")
hemoglobin()