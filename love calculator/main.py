print("WELCOME TO THE LOVE CALCULATOR")

name1 = input("enter 1st person name? ").lower()
name2 = input("enter 2nd person name? ").lower()


name = name1 + name2

T = name.count("t")
R = name.count("r")
U = name.count("u")
E = name.count("e")

sum = T + R + U + E

print(sum)

L = name.count("L") 
O = name.count("o")
V = name.count("v")
E = name.count("e")

sum2 = L + O + V + E

print(sum2)

love_score = str(sum) + str(sum2)
print(f"your love score is {love_score}")
