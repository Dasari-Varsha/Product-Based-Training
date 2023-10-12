#MERGE SORT using Inversion Count
def mergesort(l,inversion):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]#not including mid value
        right=l[mid:]#including mid
        li=mergesort(left,inversion)
        ri=mergesort(right,inversion)
        i=j=k=0  #i-index of left # j -right array index #index of res array
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                l[k]=left[i]
                i+=1
                k+=1
            else:
                l[k]=right[j]
                j+=1
                k+=1
                inversion+=len(left)-i
        while i<len(left):
           l[k]=left[i]
           i=i+1
           k=k+1
        while j<len(right):
           l[k]=right[j]
           j+=1
           k+=1
        return inversion+li+ri
    return 0
l=list(map(int,input().split()))
print(mergesort(l,0))
print(l)