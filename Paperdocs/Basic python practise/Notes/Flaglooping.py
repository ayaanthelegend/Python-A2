sum = 0 
flag = True

while flag == True:
    num = float(input("Enter the number: "))
    if num == 0:
        flag = False
    else:
        Sum = sum + num

print(sum)