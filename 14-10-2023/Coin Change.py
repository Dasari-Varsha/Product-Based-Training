#322. Coin Change
def coinChange(coins, amount):
        dp=[[float('inf') for i in range(amount+1)] for i in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0]=0
        for i in range(1,len(coins)+1):
            for j in range(1,amount+1):
                if coins[i-1]>j:
                    dp[i][j]=dp[i-1][j]
                else:
                    dp[i][j]=min(1+dp[i][j-coins[i-1]],dp[i-1][j])
        
        res= dp[len(coins)][amount]
        if res>=float('inf'):
            return -1
        else:
            return res
coins=list(map(int,input().split()))
amount=int(input())
print(coinChange(coins,amount))
