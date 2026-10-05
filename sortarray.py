# Sort an array. 
n = list(map(int, input("enter a list of numbers separated by spaces:").split()))

for i in range(len(n)):
    for j in range(0, len(n) - i - 1):
        if n[j] > n[j + 1]:
            n[j], n[j+1] = n[j+1], n[j]

print(*n)
