# intializing an Array 20 exams score 0-100 random generate

import random

#Array intalized populated with random numbers

exams_scores = []
for i in range(20):
    exams_scores.append(random.randint(0, 100))

# find lowest score, Average score and how many students scored above average score

avg = 0
lowest = 100
above_average = 0

for i in range(20):
    avg = avg + exams_scores[i]
    if exams_scores[i] < lowest:
        lowest = exams_scores[i]

avg = avg/ 20

for i in range(20):
    if exams_scores[i] > avg:
        above_average = above_average + 1

print("Lowest score:", lowest)
print("Average score:", avg)
print("Number of students who scored above average:", above_average)