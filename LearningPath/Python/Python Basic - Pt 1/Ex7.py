#Write a Python program that accepts a filename from the user and prints the extension of the file.

fileName = input("Insert file name in the format [filename].[extension]: ")

fileExt = fileName.split(".")

print("File extension is " + repr(fileExt[-1]))