seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter month (1-12): "))

if month == 12 or month == 1 or month == 2:
    print(seasons[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons[2])
else:
    print(seasons[3])