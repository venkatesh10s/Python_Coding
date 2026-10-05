# Find the product of an array except itself. 
nums = list(map(int, input("enter a list of numbers separated by spaces:").split()))

result = []

for i in range(len(nums)):
    product = 1

    for j in range(len(nums)):
        if i != j:
            product = product * nums[j]

    result.append(product)

print(*result)