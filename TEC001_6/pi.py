import random

# Ask the user for number of points
N = int(input("How many random points should be generated? "))

n = 0

for i in range(N):
    # Generate random point in the square [-1,1] x [-1,1]
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Check if the point lies inside the unit circle
    if x**2 + y**2 < 1:
        n += 1

# Calculate approximation of pi
pi_approx = 4 * n / N

print("Approximation of pi:", pi_approx)