#  largest of three numbers

a, b, c = map(int, input("enter three numbers separated by spaces: ").split())

largest = a

if b > largest:
    largest = b

if c > largest:
    largest = c

print(largest)