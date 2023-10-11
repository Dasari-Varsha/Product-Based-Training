#magic Square
#input::3
#output:2 7 6
#       9 5 1
#       4 3 8
#       magic constant: 15
n=int(input())
sq=[[0]*n for i in range(n)]
num=1
i=n//2
j=n-1
while num<=(n*n):
    if i<0 and j==n:
        i=0
        j=n-2
    else:
        if i<0:
            i=n-1
        if j==n:
            j=0
    if sq[i][j]:
        i=i+1
        j=j-2
        continue
    sq[i][j]=num
    num+=1
    i=i-1
    j=j+1
for i in sq:
    print(*i)
print("magic constant:",n*(n**2+1)//2)
