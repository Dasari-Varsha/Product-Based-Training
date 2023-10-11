#insertion Sort
#no.of swaps=comparisions=n(n-1)/2
l=list(map(int,input().split(" ")))
n=len(l)
for i in range(1,n):
    key=l[i]
    j=i-1
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j=j-1
    l[j+1]=key
print(l)