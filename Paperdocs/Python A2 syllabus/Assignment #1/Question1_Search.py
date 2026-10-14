# DECLARE Readings: ARRAY[0:15] OF INTEGER
Readings = [42, 17, 89, 42, 5, 63, 42, 91, 17, 28, 77, 42, 8, 50, 17]

def OutputReadings(readings):
    string = ""
    for i in range(len(readings)):
        string = string + str(readings[i]) + " "
    120


def LinearSearch(readings, Search_Value):
    for index in range(len(readings)):
        if readings[index] == Search_Value:
            return index
    return -1

def CountOccurences(readings, Search_Value):
    count = 0
    for i in range(len(readings)):
        if readings[i] == Search_Value:
            count = count + 1
    return count

OutputReadings(Readings)

valid = False
searchnum = 0

while valid == False:
    searchnum = int(input("Enter a whole number between 1 and 100 : "))
    if searchnum >= 1 and searchnum <= 100:
        valid = True
    else:
        print("Invalid input. Please Try again.")

first_index = LinearSearch(Readings, searchnum)
Occurences = CountOccurences(Readings, searchnum)

if first_index != -1:
    print("The value " + str(searchnum) + " was first found at index " + str(first_index) + " and appears " + str(Occurences) + " times.")
else:
    print("The value " + str(searchnum) + " is not in the array.")

def OutputAllPositions(readings, Search_Value):
    found = False
    for i in range(len(readings)):
        if readings[i] == Search_Value:
            print("Found at index " + str(i))
            found = True
    if found == False:
        print("Not Found")

# testing with calling 42

OutputAllPositions(Readings, 42)