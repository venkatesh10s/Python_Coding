# character frequency count
n = input("enter a string : ")

freq = {}

for i in n:
    freq[i] =  freq.get(i, 0) + 1

for key, value in freq.items():
    print(f"{key}:{value}")    