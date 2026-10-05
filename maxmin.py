#Find the maximum and minimum values in an array.
n = list(map(int, input("enter a list of numbers separated by spaces:").split()))

min = n[0]
max = n[0]

for i in range(len(n)):
    if n[i] > max:
        max = n[i]
    
    if n[i] < min:
        min = n[i]

print("Maximum value:", max)
print("Minimum value:", min)