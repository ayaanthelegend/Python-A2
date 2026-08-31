#Write a program that counts the number of vowels, consonants, digits, and spaces in a given string.

string = input("Please enter a string: ")
stringlower = string.lower()

vowels = "aeiou"
vowelcount = 0
consonantscount = 0
Digitscount = 0
Spacescount = 0 

for char in stringlower:
    if stringlower == " ":
        Spacescount = Spacescount + 1
    elif char in vowels:
        vowelcount = vowelcount + 1
    elif '0' <= char <= '9':
        Digitscount = Digitscount + 1
    else:
        consonantscount = consonantscount + 1

print("Vowels:", vowelcount)
print("Consonants:", consonantscount)
print("Digits:", Digitscount)
print("Spaces:", Spacescount)
