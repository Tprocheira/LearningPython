#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

n = input("Write a number to calculate n+nn+nnn: ")

n_1 = n+n
n_2 = n_1+n

result = int(n)+int(n_1)+int(n_2)

print(n)
print(n_1)
print(n_2)
print(result)
