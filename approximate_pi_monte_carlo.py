import random

points = int(input("How many points: "))

inside = 0

for i in range(points):

    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x*x + y*y < 1:
        inside += 1

pi = 4 * inside / points

print("Approximate pi:", pi)