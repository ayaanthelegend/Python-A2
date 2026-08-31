#Write a Python program to store 5 student names in a 1D array. Then ask the user to 
#enter an index and output the name stored at that index.

student_names = ["Ayaan", "Bilal", "Wassay", "Raqim", "Hamza"]

index = int(input("Please enter an index from 0-4: "))

if index >= 0 and index < len(student_names):
    print("The name stored at index", index, "is", student_names[index])
else:
    print("Invalid index. Please enter an index from 0-4.")
