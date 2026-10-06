# Second Largest Distinct Value

n = int(input("enter a number : "))

a = list(map(int, input("enter a list of numbers : ").split()))

result = sorted(set(a), reverse = True)

print(result[1])