#valid palindromes in a string
#INPUT:abbaa
#OUTPUT:['abba', 'aa']
str=input()
res=[]
def ispal_rev(left,right):
    n=len(str)
    while left>=0 and right<n and str[left]==str[right]:
        left-=1
        right+=1
    return str[left+1:right]
for i in range(len(str)):
    pal1=ispal_rev(i,i)
    if len(pal1)>1:
        res.append(pal1)
    pal2=ispal_rev(i,i+1)
    if len(pal2)>1:
        res.append(pal2)
print(res)