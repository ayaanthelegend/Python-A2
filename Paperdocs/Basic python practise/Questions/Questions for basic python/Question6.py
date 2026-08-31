word = input("Enter a word: ")

lenword = len(word) # length of the word

for char in word[0]:
    firstletter = word[0]
    lastletter = word[lenword-1]

print(lenword)
print(firstletter)
print(lastletter)
