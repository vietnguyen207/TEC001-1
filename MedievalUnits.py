# Medieval units calculation
t = float(input("Enter talents: "))
pd = float(input("Enter pounds: "))
ls = float(input("Enter lots: "))
tpl = t*20*32*13.3 + pd*32*13.3 + ls*13.3
kg = tpl // 1000
gr = tpl % 1000
print (f"The weight in modern units: {kg}Kilograms and {gr}grams")