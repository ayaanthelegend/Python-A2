Arraydata = [10,5,6,7,1,12,13,15,21,8]

def InsertionSort():
    arraysize = 10

    for pointer in range(1, arraysize):
        valuetoinsert = Arraydata[pointer]
        holeposition = pointer

        while (holeposition > 0) and (Arraydata[holeposition -1] > valuetoinsert):
            #SHIFTING
            Arraydata[holeposition] = Arraydata[holeposition -1]
            holeposition = holeposition + 1

        Arraydata[holeposition] = valuetoinsert
