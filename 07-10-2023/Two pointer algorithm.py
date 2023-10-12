#TWO-Pointer Algorithm(LEFT-RIGHT)
l=list(map(int,input().split()))
target=int(input())
l.sort()
left=0
right=len(l)-1
while left<right:
    sum=l[left]+l[right]
    if sum==target:
        print("found")
        break
    if sum<target:
        left+=1
    else:
        right-=1