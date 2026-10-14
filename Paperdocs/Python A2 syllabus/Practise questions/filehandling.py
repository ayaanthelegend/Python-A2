# find the sum of all the characters

file = open("HighScore.txt" , "r")

score = 0
for x in range(20):
    playername = file.read().strip()
    playerscore = file.read().strip()
    score = score + int(playerscore)

  
file.close()


#Strip function is used to remove the extra new line character

# If you have different values on each line

file = open("Highscore.txt" , "r")

for line in file:
    print(line.strip())
    