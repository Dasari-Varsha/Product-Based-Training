#1
#22
#333
n=int(input())
for i in range(n):
    print(str(i+1)*(i+1))
 or
n=int(input())
a=1
for i in range(1,n+1):
    print(a*i)
    a=(a*10)+1
    or
n=int(input())
for i in range(1,n+1):
    print(i*(10**i//9))