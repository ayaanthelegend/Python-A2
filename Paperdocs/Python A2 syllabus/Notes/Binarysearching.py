arrayData = [1,5,6,7,8,10,12,13,15,21]

def BinarySearch(number):
    upperbound = 9
    lowerbound = 0
    valuefound = False
    notinlist = True

    while valuefound == False and notinlist == False:
        midpoint = int((upperbound + lowerbound) / 2)

        if arrayData[midpoint] == number:
            valuefound = True
            return True
        elif arrayData[midpoint] < number:
            lowerbound = midpoint + 1
        else: 
            upperbound = midpoint - 1

        if lowerbound > upperbound:
            notinlist = True
            return False
        
