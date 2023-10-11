#generate valid parenthesis code
def generate(n):
    res=[]
    def parenthesis(s,open=0,close=0):
        if n==open==close:
            res.append(s)
        if open<n:
            parenthesis(s+'(',open+1,close)
        if close<open:
            parenthesis(s+')',open,close+1)
        return res
    return parenthesis(s="")
n=int(input())
res=generate(n)
print(res)