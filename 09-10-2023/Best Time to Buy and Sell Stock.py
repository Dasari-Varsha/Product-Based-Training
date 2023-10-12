#LEETCODE :121   Best Time to Buy and Sell Stock
#Input: prices= [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
l=list(map(int,input().split()))
maxprofit=0
buy=l[0]
for i in l:
    if i<buy:
        buy=i
    elif (i-buy)>maxprofit:
        maxprofit=i-buy
print(maxprofit)
