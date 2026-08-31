#Write a program that declares a 1D array of 10 integers, populates it with values entered 
#by the user, then outputs the sum and average. 

# declare a 1D array of 10 integers


Numbers = []
total = 0
sum = 0
average = 0

for x in range (10):
    Numbers.append(0)  # intializing the Array

for i in range(10):
    num = int(input("Please enter an integer: "))
    Numbers[i] = num

for count in Numbers:
    total = total + count

average = total / 10
print("The sum of the numbers is:", total)
print("The average of the numbers is:", average)



