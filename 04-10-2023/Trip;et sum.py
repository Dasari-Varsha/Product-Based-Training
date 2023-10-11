
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