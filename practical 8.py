# Program to read a file and write content in uppercase

# open source file
f1 = open("input.txt", "r")

# read content
data = f1.read()

# convert to uppercase
data_upper = data.upper()

# open new file
f2 = open("output.txt", "w")

# write uppercase data
f2.write(data_upper)

# close files
f1.close()
f2.close()

print("Content copied in uppercase successfully.")
# Program to copy python file without comments

# ask user for file names
source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

# open files
f1 = open(source, "r")
f2 = open(destination, "w")

for line in f1:
    # ignore comment lines
    if not line.strip().startswith("#"):
        f2.write(line)

f1.close()
f2.close()

# print source file content
print("\nSource File Content:")
f1 = open(source, "r")
print(f1.read())
f1.close()

# print destination file content
print("\nDestination File Content:")
f2 = open(destination, "r")
print(f2.read())
f2.close()