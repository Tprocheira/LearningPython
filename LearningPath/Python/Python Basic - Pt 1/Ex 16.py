#Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.

n = int(input("Input a number for calculation: "))

if (n<=17):
    print(abs(n-17))
else:
    print(2*(n-17))