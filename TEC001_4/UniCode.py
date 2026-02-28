def unicode(univc):
    if univc[:4] == univc[:4].upper():
        try:
            univco = int(univc[4:])
            return print("True")
        except ValueError:
            return print("False")
    else:
        return print("False")
univc = input("Enter a Course Code: ")
unicode(univc)