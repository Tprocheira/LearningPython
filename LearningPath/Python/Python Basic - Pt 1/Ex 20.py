#Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

string = input("Insert string to be repeated: ")
n = int(input("Insert number of repetitions (non-negative): "))

for i in range(n):
    print(string)