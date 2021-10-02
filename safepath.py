a=input().split()
n=int(a[0])
t=int(a[1])
l=[]
for i in range (n-1):
    l.append(input().split())
for i in range(0,len(l)):
    for j in range(0,2):
        l[i][j]=int(l[i][j])

c=list(map(int,input() .split()))

count=0
for i in range(0,len(l)):
    if (l[i][0]==1 and l[i][1]==6) or (l[i][0]==6 and l[i][1]==1):
        
        count=count+1
        
    elif(l[i][0] in c )or( l[i][1] in c)or ((l[i][0] in c) and( l[i][1]in c)):
        
        
        continue
    elif (l[i][0] not in c and l[i][1] not in c):
        
        print(l[i][0],l[i][1])
        sum=0
        for x in range(l[i][0],l[i][1]):
            if x not in c:
                sum =sum+1
        if sum !=0:
            count=count+1
            
    else:
            break
        
print (count)
                
