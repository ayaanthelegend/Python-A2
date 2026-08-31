Platenumber = input("Enter your vehicle plate number: ")

valid = True

if len(Platenumber) != 8:
    valid = False
else:
    for i in range(0,3):
        if Platenumber[i] != Platenumber[i].upper():
            valid = False

    if valid == True and Platenumber[3] != "-":
        valid = False

    if valid:
        for i in range(4,8):
            if Platenumber[i] not in "0123456789":
                valid = False

if valid:
    print("Valid plate number")
else:
    print("Invalid plate number")
