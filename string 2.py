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
    #11)Assign hexadecimal values
num = 255
hex_value = hex(num)

print("Hexadecimal value:", hex_value)
    #12)print double quotes 
s = "Python"

print("He said, \"", s, "\"", sep="")
    #13)ignoring escape sequence
s = r"Hello\nWorld"

print("String without escape sequence effect:")
print(s)
    #14)calculate no. of all possible substrings
s = input("Enter a string: ")
n = len(s)

total = n * (n + 1) // 2
print("Total number of substrings:", total)
    #15)reverse a string
s = input("Enter a string: ")

# Method 1: Slicing
print("Method 1:", s[::-1])

# Method 2: Loop
rev = ""
for ch in s:
    rev = ch + rev
print("Method 2:", rev)

# Method 3: reversed() function
print("Method 3:", "".join(reversed(s)))

# Method 4: While loop
rev2 = ""
i = len(s) - 1
while i >= 0:
    rev2 += s[i]
    i -= 1
print("Method 4:", rev2)

# Method 5: Recursion
def reverse_string(text):
    if len(text) == 0:
        return text
    return reverse_string(text[1:]) + text[0]

print("Method 5:", reverse_string(s))
    #16)reversing using stack
s = input("Enter a string: ")

# Using stack
stack = list(s)
rev = ""
while stack:
    rev += stack.pop()

print("Using stack:", rev)

# Using reversed()
print("Using reversed():", "".join(reversed(s)))
    #17)spliting a string
s = input("Enter a string: ")

chars = list(s)
print("List of characters:", chars)
    #18)slicing
s = input("Enter a string: ")

print("First 3 characters:", s[:3])
print("Last 3 characters:", s[-3:])
print("Middle part:", s[1:4])
    #19)repeat M characters
s = input("Enter a string: ")
m = int(input("Enter number of characters (M): "))
n = int(input("Enter number of times (N): "))

part = s[:m]
result = part * n

print("Result:", result)
    #20)swap charcaters
s = input("Enter a string: ")

if len(s) < 2:
    print("String too short to swap.")
else:
    new_s = s[-1] + s[1:-1] + s[0]
    print("After swapping:", new_s)
    #21)
s = input("Enter a string: ")
index = int(input("Enter index to remove: "))

if index < 0 or index >= len(s):
    print("Invalid index")
else:
    new_s = s[:index] + s[index+1:]
    print("After removal:", new_s)
    #22)
s = input("Enter your name: ")

message = "Welcome "
result = message + s

print(result)
    #23)
s = input("Enter a string: ")
matched = []

for ch in s:
    if s.count(ch) > 1 and ch not in matched:
        matched.append(ch)

print("Matched characters:", matched)
    #24)
s = input("Enter a string: ")

for ch in set(s):
    print(ch, ":", s.count(ch))
    #25)
s = input("Enter a string with mobile number: ")

number = ""
for ch in s:
    if ch.isdigit():
        number += ch

print("Extracted number:", number)
    #26)
text = input("Enter paragraph: ")
old = input("Enter word to replace: ")
new = input("Enter new word: ")

result = text.replace(old, new)
print("Updated text:", result)
    #27)
s = input("Enter a string: ")

for ch in s:
    print(ch, "->", ord(ch))
    #28)
s = input("Enter a string: ")

print("Reversed string:", s[::-1])
    #29)
s = input("Enter a sentence: ")
words = s.lower().split()

camel = words[0] + ''.join(word.capitalize() for word in words[1:])

print("camelCase:", camel)
    #30)
s = input("Enter a sentence: ")

result = s.title()
print("Capitalized:", result)

