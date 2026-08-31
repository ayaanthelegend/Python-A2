# Ask the user to enter a word and count how many times the letter "a" appears in the word

word = input("Please enter the word")

count = 0

for char in word:
    if char == "a":
        count = count + 1

print("The letter 'a' appears", count, "times in the word.")
