arrayData = [10,5,6,7,1,12,13,15,21,8]

#Inefficent bubble sort

def bubblesort():
    for x in range(0,10):
        for y in range(0,9):
            if arrayData[y] > arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y+1] = temp


# Efficent bubble sort

arrayData = [10,5,6,7,1,12,13,15,21,8]

def bubblesort():
    Noswaps = False
    Boundary = 9
    while Noswaps == False:
        Noswaps = True
        for y in range(0, Boundary):
            if arrayData[y] > arrayData[y+1]:
                temp = arrayData[y]
                arrayData[y+1] = temp
                Noswaps = False

        Boundary = Boundary - 1

bubblesort()
print(arrayData)