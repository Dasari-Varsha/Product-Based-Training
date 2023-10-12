#FRACTIONAL KNAPSACK
knapsack_wt=int(input("enter knapsack weight:"))
wt=list(map(int,input().split()))
pr=list(map(int,input().split()))
perkg=[]
l=list(zip(wt,pr))
l.sort(key=lambda x:x[1]/x[0],reverse=True)
print(list(l))
maxprofit=0
for weight,profit in l:
    if weight<=knapsack_wt:
        maxprofit+=profit
        knapsack_wt-=weight
    else:
        maxprofit+=knapsack_wt*(profit/weight)
        break
print(maxprofit)