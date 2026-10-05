# Replace repeated characters in a string with $. 
n = input("enter a string:")

result = []
seen = set()

for ch in n:
    if ch in seen:
        result.append("$")
    else:
        seen.add(ch)
        result.append(ch)

print("".join(result))