# Find repeating substrings in a string. 

s = input("enter a string:")

n = len(s)

for i in range(1, n//2 + 1):
    for j in range(n - i + 1):
        sub = s[j:j + i]

        if s.count(sub) > 1:
            print(sub)