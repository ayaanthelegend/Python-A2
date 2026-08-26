#Ask 3 numbers from the user and print the largest number

num1 = float(input("Enter the number:"))
num2 = float(input("Enter the number:"))
num3 = float(input("Enter the number:"))

if num1 > num2 and num1 > num3:
    print("number 1 is largest")
elif num2 > num1 and num2> num3:
    print("Number 2 is largest")
else:
    print("Number 3 is largest")