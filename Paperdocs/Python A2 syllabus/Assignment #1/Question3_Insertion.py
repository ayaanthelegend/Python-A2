# DECLARE Results : ARRAY[0:29, 0:1] OF INTEGER
Results = [[-1 for i in range(2)] for i in range(30)]
Numberofstudents = 0

def Initialise():    
    Results = [[-1 for i in range(2)] for i in range(30)]
    Numberofstudents = 0

def AddResult(studentno, mark):
    if mark < 0 or mark > 100:
        print("Invalid marks")
    elif NumberOfStudents >= 30:
        print("Not added")
    else:
        Results[NumberOfStudents][0] = studentno
        Results[NumberOfStudents][1] = mark
        NumberOfStudents = NumberOfStudents + 1
        print("Added")

Initialise()
AddResult(1042, 87)
AddResult(1007, 64)
AddResult(1119, 92)
AddResult(1063, 64)
AddResult(1088, 105)
AddResult(1050, 78)
AddResult(1031, 64)


def InsertionSort():   
    for i in range(1, Numberofstudents):
        key_student = Results[i][0]
        key_mark = Results[i][1]
        j = i - 1
        while j >= 0 and Results[j][1] < key_mark:
            Results[j + 1][0] = Results[j][0]
            Results[j + 1][1] = Results[j][1]
            j = j- 1
        Results[j + 1][0] = key_student
        Results[j + 1][1] = key_mark


def OutputResults():    
    for i in range(Numberofstudents):
        print("Student" , Results[i][0],  "mark" , Results[i][1])


Initialise()
AddResult(1042, 87)
AddResult(1007, 64)
AddResult(1119, 92)
AddResult(1063, 64)
AddResult(1088, 105)
AddResult(1050, 78)
AddResult(1031, 64)

InsertionSort()
OutputResults()



def InsertionSort():    
    for i in range(1, Numberofstudents):
        key_student = Results[i][0]
        key_mark = Results[i][1]
        j = i - 1
        while j >= 0 and (Results[j][1] < key_mark or (Results[j][1] == key_mark and Results[j][0] > key_student)):
            Results[j + 1][0] = Results[j][0]
            Results[j + 1][1] = Results[j][1]
            j = j - 1
        Results[j + 1][0] = key_student
        Results[j + 1][1] = key_mark


Initialise()
AddResult(1042, 87)
AddResult(1007, 64)
AddResult(1119, 92)
AddResult(1063, 64)
AddResult(1088, 105)
AddResult(1050, 78)
AddResult(1031, 64)

InsertionSort()
OutputResults()