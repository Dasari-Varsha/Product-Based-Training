#sqrt of num using RECURSION
def sqrt(n,si,li,floor):
    if n<0:
        return -1
    if n==1:
        return 1
    if si<=li:
        mid=(si+li)//2
        sq=mid*mid
        if sq==n:
            return mid
        elif sq<n:
            floor=mid
            return sqrt(n,mid+1,li,floor)
        else:
            li=mid-1
            return sqrt(n,si,mid-1,floor)
    return floor
n=int(input())
si=0
li=n//2
floor=-1
res=sqrt(n,si,li,floor)
print(res)