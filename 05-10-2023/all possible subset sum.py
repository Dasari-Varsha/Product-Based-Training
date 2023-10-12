#ALL POSSIBLE SUBSETS EQUAL TO SUM
def fun(l,target):
    def backtrack(start,sum,subset):
        if start==len(l)-1 and sum+l[start]==target:
            subset.append(l[start])
            res.append(subset[:])
            return
        if sum==target:
            res.append(subset[:])
            return
        if sum>target or start==len(l):
            return
        subset.append(l[start])
        backtrack(start+1,sum+l[start],subset)
        subset.pop()
        backtrack(start+1,sum,subset)
    res=[]
    backtrack(0,0,[])
    return res
l=list(map(int,input().split()))
target=int(input())
nk=fun(l,target)
for i in k:
    print(i)