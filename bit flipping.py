#bit flipping
def tog(n,pos):
    m=1<<pos
    result=n^m
    return result
num=list(map(int,input().split(" ")))
n=num[0]
pos=num[1]
result=tog(n,pos)
print(result)