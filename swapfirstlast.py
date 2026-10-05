# swap first and last element of an array
n = list(map(int, input("enter a list of numbers separated by spaces:").split()))

n[0], n[-1] = n[-1], n[0]

print(*n)