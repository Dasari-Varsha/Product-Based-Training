l=list(map(int,input().split()))
max1=max(l)
for i in range(max1,-1,-1):
    for j in l:
        if j>i:
            print("X ",end="")
        else:
            print(" ",end=" ")
    print()