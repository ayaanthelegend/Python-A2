# Create a Function for finding the largest value in an Array and then print the table for that number

Number  = [45, 34, 23 , 87 , 96 , 23]


#finding the largest number
def large(Array):
    Largest = Array[0]

    for x in range(1, len(Array)):
        if Array[x] > Largest:
            Largest = Array[x]

    return Largest

# Printing the table
def table(num):
    for x in range(11):
        ans = num * x 
        text = str(num) + " " + "X" + " " + str(x) + " " + "=" + " " + str(ans)
        print(text)

temp = large(Number)
table(temp)