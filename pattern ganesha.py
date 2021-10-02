n=int(input())
#1st row
print("*",end="")
for i in range(0,(n-3)//2):
    print(" ",end="")
for i in range(0,(n+1)//2):
    print("*",end="")
print()
for row in range(0,(n-3)//2):
    print("*",end="")
    for i in range(0,(n-3)//2):
        print(" ",end="")
    print("*")
#4th row
for i in range(0,n):
    print("*",end="")
print()
#5th and 6th row
for row in range(0,(n-3)//2):
    for i in range(0,((n-3)//2)+1):
        print(" ",end="")
    print("*",end="")
    for i in range(0,(n-3)//2):
        print(" ",end="")
    print("*") 
#7th row
for i in range(0,(n+1)//2):
    print("*",end="")
for i in range(0,(n-3)//2):
    print(" ",end="")
print("*")    
    
