#Ask the user to enter a word and a character they want to replace. Then ask for the new 
#character and output the updated word. 

word = input("Please enter a word: ").lower()
replacechar = input("Please enter the character you want to replace: ").lower()

newchar = input("Please enter the new character: ").lower()


newword = ""
for char in word:
    if char == replacechar:
        newword = newword + newchar
    else:
        newword = newword + char

print(newword)


