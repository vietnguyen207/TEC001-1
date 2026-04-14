import re
def total_num(file):
    with open(file, "r") as f:
        num = f.read()
    total_number = re.findall(r'(\d+)',num)
    numlist = []
    for i in total_number:
        numlist.append(i)
    return print(f"Total number in file text {len(numlist)}")
file = "m.txt"
total_num(file)
