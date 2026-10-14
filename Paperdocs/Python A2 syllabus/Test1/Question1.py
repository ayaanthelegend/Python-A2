#DECLARE NAMES ARRAY[1:10]
Names = [ "Sara","Ahmed","Zain", "Hina","Bilal","Fatima","Omar","Ayesha", "Danish", "Maryam",]

#DECLARE SCORES ARRAY[1:10]
Scores = [74, 42, 91, 42, 67, 88, 55, 91, 30, 79]

def OutputPlayers(Names, Scores):
    for i in range(len(Names)):
        print(Names[i] , ": " , str(Scores[i]))

def FindPlayer(NamesArray ,Searchname):    
    for i in range(len(NamesArray)):
        if NamesArray[i] == Searchname:
            return i
    return -1

def HighestScorer(Arrayscores):
    Maxindex = 0
    for i in range(1, len(Arrayscores)):
        if Arrayscores[i] > Arrayscores[Maxindex]:
            Maxindex = i
    return Maxindex

def CountAbove(Arrayscores , Threshold):
    #Counts and returns the number of scores in the array greater than the threshold
    Count = 0
    for i in range(len(Arrayscores)):
        if Arrayscores[i] > Threshold:
            Count = Count + 1
    return Count

# Main program

OutputPlayers(Names,Scores)

Search = input("Enter the player name: ")
Foundindex = FindPlayer(Names, Search)

if Foundindex != -1:
    print(Search , " scored " , str(Scores[Foundindex]))
else:
    print(Search , " is not in the list")

Firstindex = HighestScorer(Scores)
print("The highest score is " , str(Scores[Firstindex]) , " by " , Names[Firstindex])

print("-----------------------------------------------------------------------------------")

# g part

Valid = False
Scorethreshold = -1
while not Valid:
    Scorethreshold = int(input("Enter a score between 0 and 100:  "))

    if Scorethreshold >= 0 and Scorethreshold <= 100:
        Valid = True

CountAbove1 = CountAbove(Scores, Scorethreshold)
print(str(CountAbove1) + " players scored more than " + str(Scorethreshold))

