#1) Input string
s = input("Enter a string: ")

# Access and print each character
print("Characters in the string are:")
for ch in s:
    print(ch)
    
#2) sprint exact characters of a string
    s = input("Enter a string: ")

print("Original String:", s)

print("Extracted characters:")
for i in range(len(s)):
    print("Character at index", i, ":", s[i])

#3) s = input("Enter a string: ")
words = s.split()

for word in words:
    print(word, "-> Length:", len(word))
    
#4) Print EVEN length words
s = input("Enter a string: ")
words = s.split()

print("Even length words:")
for word in words:
    if len(word) % 2 == 0:
        print(word)
#5) count vowels in a string
s = input("Enter a string: ")
words = s.split()

print("Even length words:")
for word in words:
    if len(word) % 2 == 0:
        print(word)
#6) passing string value to the function
def display_string(text):
    print("String received:", text)

s = input("Enter a string: ")
display_string(s)
#7) create multiole copies os a string using multiplication operator
s = input("Enter a string: ")
n = int(input("Enter number of times: "))

result = s * n
print("Result:", result)
#8) appending text at the end of the string using += operator
s = input("Enter a string: ")
extra = input("Enter text to append: ")

s += extra
print("After appending:", s)
#9) concatenaye two strings using + operator
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

s3 = s1 + s2
print("Concatenated string:", s3)
#10)check if a string is present using in operator
s = input("Enter main string: ")
sub = input("Enter substring to search: ")

if sub in s:
    print("Substring is present")
else:
    print("Substring is NOT present")