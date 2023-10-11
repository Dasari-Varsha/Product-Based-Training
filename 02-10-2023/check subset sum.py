#Check subset sum
def fun(l,target,n):
    if target==0:
        return True
    if n==0:
        return False
    if l[n-1]>target:
        return fun(l,target,n-1)
    return fun(l,target-l[n-1],n-1) or fun(l,target,n-1)
l=list(map(int,input().split(" ")))
target=int(input())
result=fun(l,target,len(l))
print(result)