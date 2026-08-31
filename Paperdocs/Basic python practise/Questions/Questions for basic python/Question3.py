string = input("Enter the text : ")

Flag = True
firstlen = 0
index = 0

# captalizing the first letter of each word in the string without using title() function

while Flag == True:
    character = string[index]
    if character == " ":
        Flag = False
    else: 
        firstlen = firstlen + 1
        index = index + 1

captalizedstring = string[character:firstlen].upper() + string[firstlen: len(string)]

print(captalizedstring)

