fileName = input("Insert file name in the format [filename].[extension]: ")

fileExt = fileName.split(".")

print("File extension is " + repr(fileExt[-1]))