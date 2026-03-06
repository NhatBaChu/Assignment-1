numbers = []

while True:
    n = input("Enter number: ")
    
    if n == "":
        break
    
    numbers.append(int(n))

numbers.sort(reverse=True)

print("Five largest numbers:")
for i in numbers[:5]:
    print(i)