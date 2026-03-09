n = 5

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

n = 5

for i in range(1, n+1):
    for j in range(i):
        print(i, end="")
    print()
n = 5

for i in range(1, n+1):
    for j in range(i,0,-1):
        print(j, end="")
    print()
n = 5

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j%2,end="")
    print()
    num = 2
n = 4

for i in range(1,n+1):
    for j in range(i):
        print(num,end=" ")
        num += 2
    print()
n = 5

for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()
    n = 4

for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
letters = ['p','y','t','h','o']

for i in range(len(letters)):
    for j in range(i+1):
        print(letters[i],end="")
    print()
word = "python"

for i in range(len(word)):
    for j in range(i+1):
        print(word[j],end="")
    print()
    n = int(input())

for i in range(1,n+1):
    print(i,end="")
n = 5

for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
n = 5

for i in range(1,n+1):
    
    for j in range(n-i):
        print(" ",end=" ")
        
    for j in range(2*i-1):
        print("*",end=" ")
        
    print()
start = int(input("Enter first number: "))
end = int(input("Enter second number: "))

num = start

while num <= end:
    
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            print(num,end=" ")
            
    num += 1
