#Read the file, it reads entire file
file = open("filehandling.txt", "r")
print(file.read())
file.close()

#readline, it reads only one line
file = open("filehandling.txt", "r")
print(file.readline())
file.close()

#readlines, it reads all lines into a list
file = open("filehandling.txt", "r")
print(file.readlines())
file.close()

#read the file using with statement
with open("filehandling.txt", "r") as file:
    print(file.read())
    print("file is closed")

#write the file using with
with open("filehandling.txt", "w") as file:
    file.write("hello python")


#write
f = open("filehandling1.txt", "w")
f.write("my name is anjali")
f.close()

#write the file using with statement
with open("filehandling1.txt", "w") as file:
    file.write("hello python")
    print("file is closed")

#append
f = open("filehandling1.txt", "a")
f.write("good afternoon")
f.close()

#append using with statement
with open("filehandling1.txt", "a") as file:
    file.write("hello python")
    print("file is closed")

# r+ mode, opens the file for both reading and writing
with open("filehandling1.txt", "r+") as file:
    file.write("hello python")
    print("file is closed")

# w+ mode, opens the file for both reading and writing, truncates the file
with open("filehandling1.txt", "w+") as file:
    file.write("hello python")
    print("file is closed")

# a+ mode, opens the file for both reading and writing, appends the file
with open("filehandling1.txt", "a+") as file:
    file.write("hello python")
    print("file is closed")