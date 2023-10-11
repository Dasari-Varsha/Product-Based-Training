#binary to decimal conversion
n=int(input("Enter the number:"))
s=0
i=0
while n!=0:
    r=n%10
    s=s+r*(2**i)
    n//=10
    i=i+1
print(s)