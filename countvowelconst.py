n = input("enter a string: ")

s = set("aeiou")
vowel = 0
const = 0

for i in n:
    if i.isalpha():
        if i in s:
            vowel += 1
        else:
            const += 1

print("vowel:", vowel)
print("consonant:", const)