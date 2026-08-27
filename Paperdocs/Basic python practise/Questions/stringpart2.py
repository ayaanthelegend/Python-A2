# Seperate the First name and the Last name after taking the full name as input

Fullname = input("Please enter your name: ")

name = Fullname.split(" ")
Firstname = name[0]
Lastname = name[1]

print(Firstname)
print(Lastname) 