#Declare an Array ( 500 ELEMENTS) sdtring Names and store Bano on 325th index

# you are suppose to make intial empty Array ("") for string and (0) for integer

# DECLARE NAMES: ARRAY[0:499] OF STRING  (must write to make the examiner happy)

# METHOD 1 (Multiplication method)

Names = [""] * 500
Names[325] = "Bano"
print(Names)

# this method dosent work for object oriented programming hence method 2 is more viable and better to use

# METHOD 2 ( Append method)

Names = []

for x in range (500):
    Names.append("")  # intializing the Array

Names[325] = "Bano"
print(Names)