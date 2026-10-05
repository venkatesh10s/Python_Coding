# Swap even and odd indexed elements
n = list(map(int, input("enter a list of numbers separated by spaces:").split()))

for i in range(0, len(n) - 1, 2):
    n[i], n[i+1] = n[i+1], n[i]

print(*n)