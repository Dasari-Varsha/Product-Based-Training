#THREE POINTER ALGORITHM - Triplet sum
l=list(map(int,input().split()))
target=int(input())
l.sort()
for i in range(len(l)):
    left=i+1
    right=len(l)-1
    while left<right:
        sum=i+l[left]+l[right]
        if sum==target:
            print("Found")
            break
        if sum<target:
            left+=1
        else:
            right-=1