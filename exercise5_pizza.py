# Exercise 5: Pizza value comparison

import math

def pizza_unit_price(diameter, price):
    radius = diameter / 2
    area = math.pi * radius * radius
    return price / area

def compare_pizza():
    d1 = float(input("Enter diameter of pizza 1: "))
    p1 = float(input("Enter price of pizza 1: "))

    d2 = float(input("Enter diameter of pizza 2: "))
    p2 = float(input("Enter price of pizza 2: "))

    unit1 = pizza_unit_price(d1, p1)
    unit2 = pizza_unit_price(d2, p2)

    if unit1 < unit2:
        print("Pizza 1 provides better value for money.")
    elif unit2 < unit1:
        print("Pizza 2 provides better value for money.")
    else:
        print("Both pizzas have the same value.")

compare_pizza()
