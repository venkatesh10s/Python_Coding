#check palindrome number using slicing
n = input("enter a string:")

if n == n[::-1]:
    print(n, "is a palindrome")
else:
    print(n, "is not a palindrome")

# check palindrome using loop
n = input("enter a string:")

left = 0
right = len(n) - 1
palindrome = True

while left < right:
    if n[left] != n[right]:
        palindrome = False
        break
    left += 1
    right -= 1

if palindrome:
    print("palindrome")
else:
    print("not a palindrome")


#check palindrome using loop
n = int(input("enter a number:"))

original = n
reversed = 0

while n > 0:
    digit = n % 10
    reversed = reversed * 10 + digit
    n = n // 10

if original == reversed:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

# check palindrome using recursion

def palindrome(s, left, right):

    if left >= right:
        return True
    
    if s[left] != s[right]:
        return False

    return palindrome(s, left + 1, right - 1)

s = input("enter a number:")

if palindrome(s, 0, len(s) - 1):
    print("It is a palindrome")
else:
    print("It is not a palindrome")

# check palindrome using two pointer
s = input()

left = 0
right = len(s) - 1

while left < right:
    if s[left] != s[right]:
        print("not a palindrome")
        break
    left += 1
    right -= 1
else:
    print("palindrome")

    