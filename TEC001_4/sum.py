import re

def sum_numbers(paragraph):
    numbers = re.findall(r'\d+', paragraph)
    total = sum(int(num) for num in numbers)
    return total
paragraph = input("Enter a paragraph: ")
sum_numbers(paragraph)
