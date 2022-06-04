height = input("enter heights of students? ").split()

'''list_of_height = height.split()
print(list_of_height)
list = []
for i in list_of_height:
    print(int(i))
    list.append(int(i))
print(list)'''


for n in range(0,len(height)):
    height[n]=int(height[n])

sum = 0
for i in height:
    sum += i
print(sum)

no_students = 0
for j in height:
    no_students +=1
print(no_students)
    
avrg = sum/no_students
print(avrg)