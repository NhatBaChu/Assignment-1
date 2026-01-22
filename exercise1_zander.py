def zander():
    length = int(input("Enter the length of the zander: "))

    if length < 42:
        diff = 42 - length
        print("Release the fish back into the lake.")
        print("The fish is", diff, "cm below the size limit.")
    else:
        print("The fish meets the size limit.")
