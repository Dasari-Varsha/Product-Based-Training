#sum of the array elements using DIVIDE AND CONQUER Algorithm
def sum1(l,si,li):
    if si==li:
        return l[si]
    if si>li:
        return -1
    mid=(si+li)//2
    return sum1(l,si,mid)+sum1(l,mid+1,li)
l=list(map(int,input().split()))
n=len(l)
res=sum1(l,0,n-1)
print(res)