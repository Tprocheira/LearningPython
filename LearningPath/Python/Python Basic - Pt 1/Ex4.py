#4. Write a Python program that calculates the area of a circle based on the radius entered by the user.

from math import pi

rad = float(input("Insert circle radius: "))

area = pi*rad**2

print(area)
