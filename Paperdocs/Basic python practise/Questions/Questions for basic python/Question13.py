# Declare Temperature Array of 7 real numbers representing daily temperatures for a 
# week. Write an algorithm that: 
 
# -  outputs the day number (1–7) with the highest temperature 
# -  calculates how many days had a temperature above 25.0 
# -  reverses the array in place (without using reverse()) 

Temperature = []

for x in range (7):
    Temperature.append(0)  # Initialize the array

for i in range(7):
    Temperature[i] = float(input("Enter temperature for day: "))

highest_temp = 0
highest_temp = Temperature[0]

for i in range(1, 7):
    if Temperature[i] > highest_temp:
        highest_temp = Temperature[i]
        highest_day = i + 1

print("Day with highest temperature:", highest_temp)

above25 = 0
for temp in Temperature:
    if temp > 25.0:
        above25 = above25 + 1

print("Number of days with temperature above 25:", above25)

# Reversing the array in place
for i in range(7 // 2):
    Temperature[i], Temperature[6 - i] = Temperature[6 - i], Temperature[i]

print("Temperature array after reversing:", Temperature)


