#count good numbers
import math
n=int(input("Enter the number:"))
mod=10**9+7
odd=(n+1)//2
even=n//2
result=(pow(5,odd,mod)*pow(4,even,mod))%mod
print(result)