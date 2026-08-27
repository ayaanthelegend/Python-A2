# Seperate the First name and the Last name after taking the full name as input

Fullname = input("Please enter your name: ")

Flag = True
firstlen = 0
index = 0

while Flag == True:
    character = Fullname[index]
    if character == " ":
        Flag = False
    else: 
        firstlen = firstlen + 1
        index = index + 1 

lastlen = len(Fullname) - (firstlen + 1)

Firstname = Fullname[0:firstlen]
Lastname = Fullname[firstlen + 1: len(Fullname)]

print(Firstname)
print(Lastname)

Fullname.split