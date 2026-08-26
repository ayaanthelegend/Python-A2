# Declaring variables 

Num = 54.7
Numwhole = int(Num)
print(Numwhole)


# converting data types 

# String based real number cannot be converted into integer directly
# String based real number --> floating ( real) ---> int()

Num = 54.7
Numwhole = float(Num)
numinteger = int(Numwhole)
print(numinteger)

# String based Integer number can be converted into real number directly

Num = "54"
number = float (Num)
print(number)

# Integer to String
# Concatentation ( string combine )

Number = 54
StringNumber = str(Number)
print ( type(StringNumber))


# input with IF statements

usernumber = float(input("Guess the number"))

if usernumber == 20:
    print("Dsadsadsads")
print("dsasad")

#input with else IF statements

if usernumber == 20:
    print("Dsadsadsads")
else: 
    print("you cant do this shi")
print("you guessed it")


# If statements with elif


if usernumber == 20:
    print("Dsadsadsads")
elif usernumber == 21: 
    print("you cant do this shi")
else:
    print("Elseif general syntax")
print("you guessed it")