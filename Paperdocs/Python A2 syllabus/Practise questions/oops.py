class Balloon:
    #PRIVATE Health : INTEGER
    #PRIVATE Colour : STRING
    #PRIVATE DefenceItem : STRING
    def __init__(self, ColourP, DefenceP):
        self.__Colour = ColourP
        self.__DefenceItem = DefenceP
        self.__Health = 100

    def GetDefenceItem(self):
        return self.__DefenceItem

    def ChangeHealth(self, change):
        self.__Health = self.__Health + change

    def CheckHealth(self):
        if self.__Health <= 0: 
            return True
        else:
            return False


userdefence = input("Enter the defence item: ")
usercolour = input("Enter the colour")

Balloon1 = Balloon(usercolour, userdefence)


def Defend(BalloonObject):
    userstrength = int(input("Enter the strength: "))
    BalloonObject.ChangeHealth(-userstrength)

    temp = BalloonObject.GetDefenceItem()
    print("The Defence Item Is:", temp)

    flag = BalloonObject.CheckHealth()

    if flag == True:
        print("No Health Remaining")
    else:
        print("Health Remaining")

    return BalloonObject


Balloon1 = Defend(Balloon1)

class Lesson:
    #PRIVATE LessonType : STRING
    #PRIVATE Instructor : STRING
    
    def __init__(self, Lesson, Instr):
        self.__LessonType = Lesson
        self.__Instructor = Instr

    def GetLessonType(self):
        return self.__LessonType

    def GetFee(self, Level):
        if Level == 'A':
            return 55
        elif Level == 'B':
            return 45
        elif Level == 'I':
            return 50
        else:
            return -1


# YOU ARE NOT SUPPOSE TO USE THE CONCEPT OF MULTIPLICATION IN ARRAY OF OBJECT

#DECLARE LessonArray : ARRAY[0:8] OF Lesson
LessonArray = []   
for x in range(9):
    LessonArray.append(Lesson("", ""))

MyLesson = Lesson("Improve Your Serve", "David")
LessonArray[2] = MyLesson

temp = LessonArray[2].GetLessonType()
print(temp)
