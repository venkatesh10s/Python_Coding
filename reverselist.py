#reverse the list using two pointer
s = list(map(int, input("enter a list of numbers separated by spaces:").split()))

left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1

print(*s)

# sort the list in descending order using built in functions
s  = list(map(int, input("enter a list of numbers separated by spaces:").split()))

s = sorted(s, reverse = True)

print(*s)