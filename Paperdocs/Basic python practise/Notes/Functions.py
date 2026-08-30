#basic function defining

def Greet(name):
    final = "Hello" + " " + name
    print(final)

# Calling the function

Greet("Bano")
Greet("Taha")

# example 2

def Add(Number1,Number2):
    Ans = Number1 + Number2
    print(Ans)

Add(5,2)

#Example 3 return function

def Pizza(item1,item2):
    ans = item1 + " " + item2
    return ans

Kitchen = Pizza("Chicken", "Olives")
print(Kitchen + " " + "Chilli")