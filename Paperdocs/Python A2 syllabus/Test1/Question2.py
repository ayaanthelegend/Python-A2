#DECLARE DataArray: ARRAY[1:12]
DataArray = [58, 12, 93, 7, 41, 19, 76, 25, 60, 3, 88, 34]


def OutputArray(Array):
    Output = " "
    for i in range(len(Array)):
        Output = Output + str(Array[i]) + " "
    print(Output.strip())


def InsertionSort(Array):
    for i in range(1, len(Array)):    
        j = i - 1        
            
    return Array


def BinarySearch(DataArray, Find):
    Low = 0
    High = len(DataArray) - 1
    Comparison = 0
    Foundindex = -1

    while Low <= High:
        Mid = (Low + High) // 2
        Comparison = Comparison + 1
        if DataArray[Mid] == Find:
            Foundindex = Mid            
        elif DataArray[Mid] < Find:
            Low = Mid + 1
        else:
            High = Mid - 1

    print("Comparison: " + str(Comparison))
    return Foundindex


def LinearCount(Arr, ToFind):
    Comparisons = 0
    for i in range(len(Arr)):
        Comparisons = Comparisons + 1
        if Arr[i] == ToFind:
            return Comparisons
    return Comparisons


# Main Program

OutputArray(DataArray)
DataArray = InsertionSort(DataArray)
OutputArray(DataArray)

Search = int(input("Enter a number to find (-1 to stop): "))

while Search != -1:
    Result = BinarySearch(DataArray, Search)
    if Result != -1:
        print(str(Search) + " found at index " + str(Result))
    else:
        print(str(Search) + " not found")

    Lowestcount = LinearCount(DataArray, Search)
    print("Linear search comparisons: " + str(Lowestcount))

    Search = int(input("Enter a number to find (-1 to stop): "))