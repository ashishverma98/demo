dict = { 1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6, 0:6}

number = input("enter any number: ")

print(number)
n = len(number)

def function(n, number):
    x = int(number)
    i=0 
    l =[]

    while i<n:
        new_number =x%10
        l.append(new_number)

        x = int(x/10)
        i+=1


    sum = 0

    for i in l:
        a = dict[i]
        sum = sum + a

    print(sum) 

function(n, number)
