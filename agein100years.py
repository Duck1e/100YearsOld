#This will import datetime library and timedelta module
import datetime
from datetime import date, timedelta

now = datetime.date.today().year

#This will collect the user input for their age

age = int(input("Enter your age:"))

#Time to do the math!

years = 100
math = (100-(age))
total = ((now)+(math))

print(total)