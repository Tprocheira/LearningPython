#Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

valueList = input("Insert list of items (comma separated): ")

list1 = valueList.split(",")
tuple1 = tuple(list1)

print(list1)    
print(tuple1)