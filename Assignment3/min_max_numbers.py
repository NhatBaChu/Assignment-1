smallest = None
largest = None

while True:
    s = input()
    if s == "":
        break
    n = int(s)
    if smallest is None or n < smallest:
        smallest = n
    if largest is None or n > largest:
        largest = n

print(smallest)
print(largest)
