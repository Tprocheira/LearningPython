#  Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.

text = input("Insert a string: ")
n = int(input("Define number n: "))
i=0

if len(text) < 2:
    while i < n:
        print(text)
        i+=1
else:
    while i < n:
        print(text[:2])
        i+=1