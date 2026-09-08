Names = ["Ayaan" ,"Bilal", "Drugs" , "Bano"]

flag = False
x = 0

while x < len(Names) and flag==False:
    if Names[x] == "Bano":
        flag = True
    else:
        x = x + 1

if flag == False: 
    print("Not found")
else:
    print("Bano is at position", x)
    

      