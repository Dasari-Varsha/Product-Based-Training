#fibonnic
def fib(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter the number:"))
for i in range(n):
    res=fib(i)
    print(res)