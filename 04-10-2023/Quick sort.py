#Quick Sort
#stable sorting technique
def quick_sort(l,start,end):
    pi=l[end]
    i=start-1
    for j in range(start,end):
        if l[j]<pi:
            i=i+1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[end]=l[end],l[i+1]
    return i+1

def quick(l,start,end):
    if start<end:
        pi=quick_sort(l,start,end)
        quick(l,start,pi-1)
        quick(l,pi+1,end)
        
l=list(map(int,input().split(" ")))
n=len(l)
quick_sort(l,0,n-1)
print(l)
