#Write a program that takes a string input and outputs:
#its length
#the string in uppercase and lowercase
#the string reversed 

user = input("Enter the string:")
length = len(user) # Length of input string

uppercase = user.upper() 
lowercase = user.lower()

stringreverse = user[::-1]

print(length)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)

#print("Length:", len(user))
#print("Uppercase:", user.upper())
#print("Lowercase:", user.lower())


print("String Reversed:", stringreverse)

