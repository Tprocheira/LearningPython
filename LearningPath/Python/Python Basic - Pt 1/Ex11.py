#Write a Python program that prints the calendar for a given month and year.

import calendar

y = int(input("Enter year number: "))
m = int(input("Enter month number: "))

print(calendar.month(y, m))