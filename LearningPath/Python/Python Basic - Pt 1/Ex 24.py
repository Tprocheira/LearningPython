#  Write a Python program to test whether a passed letter is a vowel or not.

vowels = ["a", "e", "i", "o", "u"]

def isVowel(a):
    if a in vowels:
        print(a + " is a vowel.")
    else:
        print (a + " is not a vowel.")


test = input("Input a letter: ")
isVowel(test)
