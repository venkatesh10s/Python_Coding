# apporach1
s = input("enter a string:")
s = s[::-1]
print("reverse of a string:", s)

#2. Reverse a string using a while loop.
n = input("enter a string:")

Reverse = ""

i = len(n) - 1

while i >= 0:
    Reverse += n[i]
    i -= 1

print(Reverse)

#2. Reverse a string using a for loop.
n = input("enter a string:")

Reverse = ""

for ch in n:
    Reverse = ch + Reverse

print(Reverse)

#2. Reverse a string using a while loop.
n = int(input("enter a number:"))

Reverse = 0

while n > 0:
    digit = n % 10
    Reverse = Reverse * 10 + digit
    n //= 10

print(Reverse)

# Reverse a string without reversing the characters of each word

n = input("enter a string:").split()

n = n[::-1]

print(" ".join(n))
