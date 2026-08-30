# Create a Function to display the table of the number which is passed as a perimter

def table(num):
    for x in range(11):
        ans = num * x 
        text = str(num) + " " + "X" + " " + str(x) + " " + "=" + " " + str(ans)
        print(text)

table(2)