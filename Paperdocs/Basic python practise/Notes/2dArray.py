# basic array 2d intializationa and printing the Array

Array2d = [[0,0,0,0] , [0,0,0,0] , [0,0,0,0] , [0,0,0,0] , [0,0,0,0]]

for x in range(5):
    print(Array2d[x])


#Accessing 2d Array individual elements

Array2d[3][2] = 5

for rows in range(5):
    print(Array2d[rows])

# Accessing elements in loops

for rows in range(5):
    for col in range(4):
        Array2d[rows][col] = 1 

# 40 cols and 500 rows declaring 2D array in p4

Empty2D = [[0] * 40 for i in range(500)]

for rows in range(500):
    print(Empty2D[rows])