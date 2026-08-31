#Write a Python program to input 5 numbers from the user and store them in a 1D array. 
#After all the numbers have been entered, use a loop to calculate and output the total of 
#all the numbers. 

numbers = []

for i in range(5):
    num = int(input("Please enter a number: "))
    numbers.append(num)

total = 0

for num in numbers:
    total = total + num

print("The total of all the numbers is:", total)

