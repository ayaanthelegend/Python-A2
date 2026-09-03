#Write a program that takes a string input and outputs:
#its length
#the string in uppercase and lowercase
#the string reversed 

user = input("Enter the string:")
length = len(user) # Length of input string

uppercase = user.upper() 
lowercase = user.lower()

print(length)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
#test  the commit

#print("Length:", len(user))
#print("Uppercase:", user.upper())
#print("Lowercase:", user.lower())

stringreverse = user[::-1] #this is not the correct way to do it in CS P4. They want to test the logic of string operation 
print("String Reversed:", stringreverse)

#Using while loop to reach at the end and then traverse back char by char. String is an array anyway hence can use user[i]
reversed_text = ""
i = len(user) - 1
while i >= 0:
    reversed_text = reversed_text + user[i]
    i = i - 1
print("String Reversed by Bilal:", reversed_text)
