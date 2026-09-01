#Write a program that takes a sentence and capitalises the first letter of every word (without using .title()).

#string = input("Enter the text : ")
#Flag = True
#firstlen = 0
#index = 0

# captalizing the first letter of each word in the string without using title() function
#while Flag == True:
#    character = string[index]
#    if character == " ":
#        Flag = False
#    else:
#        firstlen = firstlen + 1
#        index = index + 1

#captalizedstring = string[character:firstlen].upper() + string[firstlen: len(string)]
#print(captalizedstring)

sentence = input("Enter a sentence: ") #ayaan bilal isl
words = sentence.split(" ")

result = ""
for i in range(len(words)):
    word = words[i]
    if len(word) > 0:
        capitalised = word[0].upper() + word[1:].lower()
    else:
        capitalised = word
    
    if i > 0:
        result = result + " "
    result = result + capitalised

print("Result:", result)



