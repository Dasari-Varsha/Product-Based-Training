#check the number is  2 or not
n=int(input("Enter the number:"))
count=0
if n==1:
    print("number is power of 2")
else:
    for i in range(n//2):
        if 2**i==n :
            print("number is power of 2")
            count=1
            break      
    if(count==0):
        print("number is NOT power of 2 ")
   OR
n=int(input("Enter"))
count=0
while(n):
    count+=1
    n=n&(n-2)
if count==1:
    print("True")
else:
    print("False")