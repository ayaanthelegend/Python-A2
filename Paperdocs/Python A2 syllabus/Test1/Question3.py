# DECLARE Results : ARRAY[0:19, 0:2] OF INTEGER
Results = [[-1 for j in range(3)] for i in range(20)]
Numberofrunners = 0


def Initialise():
    global Results, Numberofrunners
    for i in range(20):
        for j in range(3):
            Results[i][j] = -1
    Numberofrunners = 0


def AddRunner(Runnerno, Category, Time):
    global Results, Numberofrunners

    if Category not in [1, 2, 3]:
        print("invalid category")
    elif Numberofrunners >= 20:
        print("Race is full")
    else:
        Results[Numberofrunners][0] = Runnerno
        Results[Numberofrunners][1] = Category
        Results[Numberofrunners][2] = Time
        Numberofrunners = Numberofrunners + 1
        print("Added")

def Bubblesort():
    global Results, Numberofrunners
    for i in range(Numberofrunners - 1):
        for j in range(Numberofrunners - 1 - i):
            if Results[j][2] > Results[j + 1][2]:
                Temp = Results[j]
                Results[j] = Results[j + 1]
                Results[j + 1] = Temp

def OutputResults():
    global Results , Numberofrunners
    for i in range(Numberofrunners):
        print("Runner ",str(Results[i][0])," category ",str(Results[i][1]) ," time " ,str(Results[i][2]))


# Main Program

Initialise()
AddRunner(207, 2, 754)
AddRunner(113, 1, 802)
AddRunner(342, 3, 699)
AddRunner(158, 4, 710)
AddRunner(291, 2, 688)
AddRunner(126, 1, 754)
AddRunner(305, 3, 731)
AddRunner(184, 1, 665)



Bubblesort()
OutputResults()
