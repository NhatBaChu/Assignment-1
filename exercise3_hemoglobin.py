def hemoglobin():
    sex = input("Enter sex (male/female): ")
    hb = int(input("Enter hemoglobin value: "))

    if sex == "female":
        if hb < 117:
            print("Hemoglobin level is low.")
        elif hb > 155:
            print("Hemoglobin level is high.")
        else:
            print("Hemoglobin level is normal.")

    elif sex == "male":
        if hb < 134:
            print("Hemoglobin level is low.")
        elif hb > 167:
            print("Hemoglobin level is high.")
        else:
            print("Hemoglobin level is normal.")
