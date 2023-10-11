#check the number power is  4 or not
n=int(input("Enter the number:"))
count=0
for i in range(n//2):
    if 4**i==n:
        print("number is power of 4")
        count=1
        break      
if(count==0):
    print("number is NOT power of 4")
OR
n=int(input("Enter"))
count=0
while(n):
    count+=1
    n=n&(n-4)
if count==1:
    print("True")
else:
    print("False")