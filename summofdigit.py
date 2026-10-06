# sum of digit of a number
n = int(input("enter a number without spaces:"))

total = 0

while n > 0:
    digit = n % 10
    total += digit
    n //= 10

print(total)

# sum of array
n = list(map(int, input("enter a list of numbers separated by spaces:").split()))

total = 0 

for i in n:
    total += i

print(total)