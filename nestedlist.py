# Flatten a nested list.
n = eval(input("enter a nested list: "))
result = []

for i in n:
    for j in i:
        result.append(j)

print(result)