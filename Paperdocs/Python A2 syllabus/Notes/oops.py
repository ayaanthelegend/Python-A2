class Person:
    #PRIVATE Name : STRING
    #PRIVATE Gender: STRING
    #PRIVATE Age: INTEGER
    # Constructor
    def __init__(self , NameP , GenderP , AgeP):
        self.Name = NameP # Public Attribute
        self._Gender = GenderP #Private Atttribute
        self._Age = AgeP

Ayaan = Person("Ayaan")
Ayaan.Name = "Ali"

#Getters

def GetName(self):
    return self._Name

def GetGender(self):
    return self._Gender

def GetAge(self):
    return self._Age

# Setters

def SetName(self , NameP):
    self._Name = NameP

def SetGender(self, GenderP):
    self._Gender = GenderP

def SetAge(self, AgeP):
    self._Age = AgeP


# How to use Methods 

Mygender = Ayaan.GetGender()
print(Mygender)

MyAge = Ayaan.GetAge()
print(MyAge)


