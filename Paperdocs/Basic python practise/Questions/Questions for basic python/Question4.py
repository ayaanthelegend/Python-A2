#A string PlateNumber stores a vehicle registration in the format "ABC-1234" (3 letters, hyphen, 4 digits). 
#Write code that validates whether a given string matches this exact format, checking character by character (do not use regular expressions).

Platenumber = input("Enter your vehicle plate number: ")

valid = True

if len(Platenumber) != 8:
    valid = False
else:
    for i in range(0,3):
        if Platenumber[i] != Platenumber[i].upper(): #you are only checking upper. what abt if it is a number - BUG
        #if not Platenumber[i].isalpha() or not Platenumber[i].isupper():
            valid = False

    if valid == True and Platenumber[3] != "-":
        valid = False

    if valid:
        for i in range(4,8):
            if Platenumber[i] not in "0123456789":
            #if not Platenumber[i].isdigit():
                valid = False

if valid:
    print("Valid plate number")
else:
    print("Invalid plate number")
