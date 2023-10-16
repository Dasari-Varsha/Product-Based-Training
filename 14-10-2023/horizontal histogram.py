#Horizontal Histogram
#l=2 3 0 4 6 3 2 1
#**
#***
#
#****
#******
#***
#**
#*
l=list(map(int,input().split()))
for i in l:
    print('*'*i)
OR
l=list(map(int,input().split()))
for i in l:
    for j in range(i):
        print('*',end=" ")
    print()