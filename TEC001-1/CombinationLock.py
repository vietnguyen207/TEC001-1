import random
# Combination Lock
code_3_digit = [random.randint(0, 9) for _ in range(3)]
code_4_digit = [random.randint(1, 6) for _ in range(4)]
print("3-digit combination lock code (0–9):", code_3_digit)
print("4-digit combination lock code (1–6):", code_4_digit)