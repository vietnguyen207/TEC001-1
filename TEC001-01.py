import math
import random
def main():
    # Name input
    n = input("Enter your name: ")
    print (f"Hello, {n} ")
    # Circle circumference calculation
    r = float(input("Enter radius of a circle (meter): "))
    cc = 2*math.pi*r
    print(f"Circumference of circle is: {cc:.2f}m")
    # Rectangle Perimeter and area calculation
    l = float(input("Enter the length of rectangle (meter): "))
    w = float(input("Enter the width of rectangle (meter): "))
    p = 2*l+2*w
    a = l*w
    print (f"The perimeter of rectangle is: {p:.2f}m \nThe area of rectangle is: {a:.2f}m^2")
    # Sum, Product and average of numbers calculation
    x = int(input("Enter the first integer: "))
    y = int(input("Enter the second integer: "))
    z = int(input("Enter the third integer: "))
    s = x+y+z
    pr = x*y*z
    avr = x+y+z/3
    print (f"The sum of 3 integers is: {s} \nThe product of 3 intergers is: {pr} \nThe averacge of 3 integers is: {avr:.2f}")
    # Medieval units calculation
    t = float(input("Enter talents: "))
    pd = float(input("Enter pounds: "))
    ls = float(input("Enter lots: "))
    tpl = t*20*32*13.3 + pd*32*13.3 + ls*13.3
    kg = tpl // 1000
    gr = tpl % 1000
    print (f"The weight in modern units: {kg}Kilograms and {gr}grams")
    # Combination Lock
    code_3_digit = [random.randint(0, 9) for _ in range(3)]
    code_4_digit = [random.randint(1, 6) for _ in range(4)]
    print("3-digit combination lock code (0–9):", code_3_digit)
    print("4-digit combination lock code (1–6):", code_4_digit)
if __name__ == "__main__":
    main()