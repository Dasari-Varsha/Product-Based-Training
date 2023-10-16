
#Sliding Window Algorithm
def sliding_window(coins,window):
    i=0
    sum1=coins[0]
    j=0
    while j<len(coins):
        if sum1==target:
            print(i,j,sum1)
            break
        elif sum1>target:
            sum1-=coins[i]
            i+=1
        else:
            j+=1
            sum1+=coins[j]
coins=list(map(int,input().split()))
target=int(input())
sliding_window(coins,target)

