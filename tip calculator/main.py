##tip calculator project

total_amt = float(input("total bill? "))
num_people = float(input("how many people to spilt the bill? "))

tip = float(input("what percentage tip do you want to give 10 12 or 15\n"))

per_person = total_amt/num_people

total_tip = (total_amt/tip)/num_people

total_bill = per_person + total_tip

print("per person bill after spilting", total_bill)

