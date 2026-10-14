class taha:
    def Eat(Self):
        print("Taha is eating biryani")

    def Sleep(Self):
        print("Taha is sleeping")

    def MakeExcuse(Self):
        print("Kal se parhai shuro")

class ChotaTaha(taha):
    def PlayGames(self):
        print("playing table tennis")

# Object creation

son = ChotaTaha()
son.Sleep()