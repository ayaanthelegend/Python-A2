# DECLARE NUMBERS: ARRAY[1:20] OF INTEGER
Numbers = []
count = 0

for x in range(20):
    Numbers.append(0)  # Initializing the Array

def ReadNumbers():
    global Numbers, count
    valid = False
    while valid == False:
        quantity = int(input("Enter Quantity numbers from 1 to 20: "))
        if quantity >= 1 and quantity <= 20:
            count = quantity
            valid = True
        else:
            print("Quantity must be between 1 and 20.")

    for i in range(count):
        num = int(input("Enter number " + str(i + 1) + ": "))
        Numbers[i] = num

def OutputNumbers():
    global Numbers, count
    string = ""
    for i in range(count):
        string = string + str(Numbers[i]) + " "
    print(string.strip())

def BubbleSort():
    global Numbers, count
    for i in range(count - 1):
        for j in range(count - 1 - i):
            if Numbers[j] > Numbers[j + 1]:
                temp = Numbers[j]
                Numbers[j] = Numbers[j + 1]
                Numbers[j + 1] = temp

def BinarySearch(ToFind):
    global Numbers, count
    low = 0
    high = count - 1
    
    while low <= high:
        mid = (low + high) // 2
        if Numbers[mid] == ToFind:
            return mid
        elif Numbers[mid] < ToFind:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1


ReadNumbers()
OutputNumbers()

BubbleSort()
OutputNumbers()

Search = int(input("Enter a number to search for: "))
iterative = BinarySearch(Search)

if iterative != -1:
    print("Found at index " + str(iterative))
else:
    print(str(Search) + " is not in the list")