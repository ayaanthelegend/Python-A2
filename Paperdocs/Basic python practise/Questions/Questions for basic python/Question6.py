### Ask the user to enter a word. Output the first character, the last character, and the total number of characters in the word.

word = input("Enter a word: ")

lenword = len(word) # length of the word

for char in word[0]:
    firstletter = word[0]
    lastletter = word[lenword-1]

print(lenword)
print(firstletter)
print(lastletter)
