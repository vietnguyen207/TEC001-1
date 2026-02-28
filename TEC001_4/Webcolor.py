def hex_color(hex):
    if len(hex) != 7 or hex[0] != "#":
        return print("Not a hex color")
    hexa = "0123456789ABCDFabcdf"
    for i in hex[:1]:
        if i not in hexa:
            return print("Not a hex color")
    return ("This is a hex color")
hex = input("Enter a hex color: ")
hex_color(hex)