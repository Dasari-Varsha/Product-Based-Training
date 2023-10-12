#sqrt of num
n=int(input())
si=0
li=n//2
floor=-1
while si<=li:
    mid=(si+li)//2
    sq=mid*mid
    if sq==n:
        floor=mid
        break
    elif sq<n:
        floor=mid
        si=mid+1
    else:
        li=mid-1
print(floor)