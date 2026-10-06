# Remove Duplicate Characters, Keep Order

n = input("enter a string:")

seen = set()
result = []

for i in n:
    if i not in seen:
        seen.add(i)
        result.append(i)

print("".join(result))