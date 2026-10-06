# sum and average of numbers using built in functions
n = int(input("enter a number : "))

s = list(map(int, input("enter a list of numbers separated by spaces: ").split()))

s = sum(s)
a = s / n

print(f"sum : {s}")
print(f"average : {a}")



# sum and average of numbers using loops
n = int(input("enter a number:"))

s = list(map(int, input("enter a list of numbers: ")))

total = 0

for i in s:
    total += i

avg = total / n

print(f"sum : {total}")
print(f"average : {avg}")

