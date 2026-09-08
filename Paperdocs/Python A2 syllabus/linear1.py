#A program stores the following integers in a global 1D array called Numbers: Numbers = [12, 7, 25, 18, 30, 9, 41, 16] Write Python program code to create a function called linearSearch() that takes an integer as a parameter and performs a linear search on Numbers. The function should return True if the value is found and False if it is not found. The main program should ask the user to input an integer, pass this value to linearSearch(), and output "Value found" if the function returns True, otherwise output "Value not found".


# DECLARE Numbers : ARRAY[0:7] OF INTEGER
Numbers = [12, 7, 25, 18, 30, 9, 41, 16]


def linearSearch(SearchValue):
    # DECLARE Found : BOOLEAN
    # DECLARE x : INTEGER

    Found = False

    for x in range(len(Numbers)):
        if Numbers[x] == SearchValue:
            Found = True

    return Found


# Main program

# DECLARE Value : INTEGER
# DECLARE Result : BOOLEAN

Value = int(input("Enter the value to search: "))

Result = linearSearch(Value)

if Result == True:
    print("Value found")
else:
    print("Value not found in the Array")