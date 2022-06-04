scores = input("enter the score of the students? ").split()
for score in range (0, len(scores)):
    scores[score] = int(scores[score])
print(scores)


highest_score = 0

for i in scores:
    if i>highest_score:
        highest_score=i
print(highest_score)
    

min_score = 500

for i in scores:
    if i<min_score:
        min_score=i
print(min_score)