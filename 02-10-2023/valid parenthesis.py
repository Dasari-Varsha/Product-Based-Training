#valid parenthesis
def parenthesis(result,n,i,j):
    if j==n:
        print(result)
        return
    if i<n:
        parenthesis(result+"(",n,i+1,j)
    if i>j:
        parenthesis(result+")",n,i,j+1)
n=int(input())
parenthesis("",n,0,0)
