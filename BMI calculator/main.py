## BMI calculator


##input height and weight

weight = float(input("weight of the person in kg? "))
height = float(input("enter height of the person in meters? "))


bmi = weight/height**2
print(bmi)

if bmi < 18:
    print("underweight")

elif bmi>18 and bmi<25:
    print("healthy")

elif bmi>25:
    print("overweight")

