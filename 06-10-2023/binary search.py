#BINARY SEARCH
def binary_search(l,first,last,ele):
    if first>last:
        return False 
    mid=(first+last)//2
    if l[mid]==ele:
        print("Found")
        return True
    if l[mid]<ele:
        binary_search(l,mid+1,last,ele)
    if l[mid]>ele:
        binary_search(l,first,mid-1,ele)
l=list(map(int,input().split()))
n=len(l)
ele=int(input())
res=binary_search(l,0,n,ele)
print(res)