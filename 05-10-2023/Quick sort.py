Quick Sort
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
'''
'''
#inversion count
l=list(map(int,input().split(" ")))
count=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            count+=1
print(count)



#QUICKSORT
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
        
    pivot = arr[0]
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
arr = list(map(int,input().split()))
result = quick_sort(arr)
print(result)
