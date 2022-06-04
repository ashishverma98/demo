## LIFE IN WEEKS 

from calendar import month
from decimal import ROUND_FLOOR


age = float(input("enter your age? "))

years_left = 90 - age
print(round(years_left)) 

days = years_left*365
months = years_left*12
weeks = months*4

print(f"number of days {days}, number of weeks {weeks}, number of months {months}")
