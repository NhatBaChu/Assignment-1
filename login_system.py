username = "python"
password = "rules"
count = 0

while count < 5:
    u = input()
    p = input()
    if u == username and p == password:
        print("Welcome")
        break
    count += 1

if count == 5:
    print("Access denied")
