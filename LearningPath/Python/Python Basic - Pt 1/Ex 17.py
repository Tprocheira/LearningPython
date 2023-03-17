#Write a Python program to test whether a number is within 100 of 1000 or 2000.

def nearTarget(n):
    return (abs(2000-n)<=100 or abs(1000-n)<=100)

print(nearTarget(950))
print(nearTarget(1200))
print(nearTarget(1950))
print(nearTarget(2101))
print(nearTarget(200))