#magic square using Recursion
#Input::5
#       9 3 22 16 15
#       2 21 20 14 8
#       25 19 13 7 1
#       18 12 6 5 24
#       11 10 4 23 17
magic constant: 65
def generete(n):
    sq=[[0]*n for i in range(n)]
    def fill(i,j,num):
        if num>(n*n):
            return sq
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
            return fill(i,j,num)
        sq[i][j]=num
        return fill(i-1,j+1,num+1)
    return fill(n//2,n-1,1)
n=int(input())
res=generete(n)
for i in res:
    print(*i)
print("magic constant:",n*(n**2+1)//2)
'''
'''
#triplet Sum
def fun(l,n,s):
    for i in range(0,n):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if(l[i]+l[j]+l[k]==s):
                    return l[i],l[j],l[k]
                
l=list(map(int,input().split(" ")))
s=int(input())
res=fun(l,len(l),s)
res=list(res)
print(res)