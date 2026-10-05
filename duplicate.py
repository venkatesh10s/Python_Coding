# Remove duplicate characters from a string while maintaining order
n = input("enter a string:")

result = []

seen = set()

for ch in n:
    if ch not in seen:
        seen.add(ch)
        result.append(ch)

print("".join(result))
