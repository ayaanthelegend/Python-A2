# DECLARE arrayData: ARRAY[0:9] OF INTEGER

arrayData = [10, 5, 6, 1, 12, 13, 15, 21, 8]



def linearSearch(value):
    for x in range(len(arrayData)):
        if arrayData[x] == value:
            return True
    return False

userinput = int(input("Enter the number you want to find"))
flag = linearSearch(userinput)

if flag == True:
    print("Value is found")
else:
    print("The value is not in the Array")



