#count no.of set bits in a number
n=int(input("Enter the number:"))
b=bin(n)
count=0
#print(b)
if n>0:
    b=b[2:]
    for i in range(len(b)):
        if b[i]=="1":
            count=count+1
else:
    b=b[3:]
    for i in range(len(b)):
        if b[i]=="1":
            count=count+1
print(count)
    OR
a=int(input("Enter the number:"))
count=0
while(a>0):
    if a&1:
        count+=1
    a=a>>1
print(count)