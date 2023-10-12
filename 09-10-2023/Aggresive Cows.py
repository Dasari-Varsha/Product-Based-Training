#Aggresive Cows
#input:n=5
#      k=3
#l=[5 8 6 3 1]
#output:3
def is_valid(n,k,stalls_pos,mid):
    prevcow=stalls_pos[0]
    count=1
    for i in stalls_pos:
        if (i-prevcow)>=mid:
            count+=1
            prevcow=i
    return True if k==count else False    
def solve(n,k,stalls_pos):
    stalls_pos.sort()
    si=0
    li=stalls_pos[-1]-stalls_pos[0]
    res=0
    while si<=li:
        mid=(si+li)//2
        if is_valid(n,k,stalls_pos,mid):
            res=mid
            si=mid+1
        else:
            li=mid-1
    return res
n=int(input())
k=int(input())
stalls_pos=list(map(int,input().split()))
result=solve(n,k,stalls_pos)
print(result)