import random

print("PY PASSWORD GENERATOR")

alfhabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

digit = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

symbols = ["!"," @", "#","$", "%"]

alf = int(input("how many alfhabets do you wants? "))
dig = int(input("how many digits do you want? "))
sym = int(input("how many sysblos fo you want? "))

password_list = []

for i in range(0,alf):
    password_list += random.choice(alfhabet)
for i in range(0,dig):
    password_list += random.choice(digit)
for i in range(0,sym):
    password_list += random.choice(symbols)

random.shuffle(password_list)



password =""
for i in password_list:
    password+=i
print(f"your password is: {password}")
                