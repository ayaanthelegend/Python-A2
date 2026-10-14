file = open("HighScore.txt" , "r")

for x in range(20):
    print(file.readline().strip())

#Close the file is open or you would loose the Mark
file.close()


# \n ----> New line character: that you are suppose to move to the next line