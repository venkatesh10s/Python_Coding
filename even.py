# print even or odd
n = int(input("enter a number:"))

if n % 2 == 0:
    print("even")

else:
    print("odd")


# print even or odd using for loop 

n = int(input("enter a number:"))

for i in range(0, n+1):
    if i % 2 == 0:
        print(i)

#  print even or odd using while loop

n = int(input("enter a number:"))
i = 0
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1


# print even or odd using for loop with end =" "

n = int(input("enter a number:"))

for i in range(0, n+1):
    if i % 2 == 0:
        print(i, end = " ")

# print even or odd using while loop with end =" "

n = int(input("enter a number:"))
i = 0
while i <= n:
    if i % 2 == 0:
        print(i, end = " ")
    i += 1
