import math
def pizzacalculation(d,p):
    dia = d/100
    area = dia*math.pi
    global unit
    unit = p/area
while True:
    d1 = input("Enter the diameter of a round pizza in cm for pizza1: ")
    p1 = input("Enter the price of a round pizza in USD for pizza1: ")
    try:
        d = float(d1)
        p = float(p1)
        break
    except:
        print("Invalid input \nPlease Try Again")
pizzacalculation(d,p)
pizza1 = unit
while True:
    d2 = input("Enter the diameter of a round pizza in cm for pizza1: ")
    p2 = input("Enter the price of a round pizza in USD for pizza1: ")
    try:
        d = float(d2)
        p = float(p2)
        break
    except:
        print("Invalid input \nPlease Try Again")
pizzacalculation(d,p)
pizza2 = unit
print(f"The unit price pizza1 is {pizza1:.2f} USD/m^2 \nThe unit price pizza2 is {pizza2:.2f} USD/m^2")
if pizza2 > pizza1:
    print("Pizza1 provides better value for money")
else:
    print("Pizza2 provides better value for money")
