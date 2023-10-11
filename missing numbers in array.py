#missing elements in an array
#1 2 3 4 6
#ot:5
l=list(map(int,input().split(" ")))
print(l)
x=0
for i in range(len(l)):
    x=x^i
for i in range(len(l)+1):
    x=x^i
print(x)