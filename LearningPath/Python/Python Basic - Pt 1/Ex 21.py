# Write a Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.

def isOdd(n):
    return (n%2!=0)

n = int(input("Insert a number to check if odd or even: "))

if isOdd(n):
    print(str(n) + " is odd.")
else:
    print(str(n) + " is even.")