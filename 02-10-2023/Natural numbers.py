# 10 to 1
def natural(n):
    if n==0:
        return 
    else:
        print(n)
        natural(n-1)
n=int(input("enter the number:"))
natural(n)
# 1 to 10
def natural(n):
    if n==0:
        return 
    else:
        natural(n-1)
        print(n)       
n=int(input("enter the number:"))
natural(n)