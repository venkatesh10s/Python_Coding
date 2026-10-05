#Print a square pattern using *. 
n = int(input("enter a number of rows:"))

for i in range(n):
    for j in range(n):
        print("*", end = " ")

    print()

#Print a rectangular pattern using *. 
r = int(input("enter a number of rows:"))
c = int(input("enter a number of columns:"))

for i in range(r):
    for j in range(c):
        print("*", end = " ")

    print()

#Print a hollow square pattern using *
n = int(input("enter a number of rows:"))

for i in range(n):
    for j in range(n):

        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print()

#print pyramid pattern using *
n = int(input("enter a number of rows:"))

for i in range(1, n+1):

    for j in range(n - i):
        print(" ", end = " ")
    
    for j in range(2 * i - 1):
        print("*", end  = " ")

    print()

# print diamond pattern using *
n = int(input("enter a number of rows:"))

for i in range(1, n+1):

    for j in range(n - i):
        print(" ", end = " ")
    
    for j in range(2 * i - 1):
        print("*", end  = " ")

    print()

for i in range(n-1, 0, -1):

    for j in range(n - i):
        print(" ", end = " ")
    
    for j in range(2 * i - 1):
        print("*", end  = " ")

    print()

