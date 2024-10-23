#create a list of score
scores  =[56,89,19,20,67,56,87,98,39,76,76,98,98,]
#Get highest and lowest score
#set a variable to get them
highest = 0
lowest = scores[0]

#list student and their scores
for i in range(len(scores)):
    print(f"Student{i}:{scores[i]}")
    if highest > scores[i]:
        highest = scores[i]
    if scores[i] < lowest:
        lowest = scores[i]
print()
print(f"== Attendance ==")
print(f"{len(scores)}Student took the test")
print()
print(f"== Highest ==")
print(f"The highest score is :{highest}")
print()
print(f"== lowest ==")
print(f"The lowest score is:{lowest}")

best_student = []
for i in range(len(scores)):
   if scores[i]==highest:
      best_student.append(i)

    
print()
print(f"== Attendance ==")
print(f"The highest performing students are :{best_student}")
    

    
    