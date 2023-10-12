#sqrt exact square root value
def sqrt_binary_search(number,epsilon=1e-6):
    if number<0:
        return ValueError("Cannot compute")
    if number<1:
        left,right=number,1
    else:
        left,right=0,number
    while abs(left-right)>epsilon:
        mid=(left+right)/2
        mid_sq=mid*mid
        if mid_sq<n:
            left=mid
        else:
            right=mid
    return (left+right)/2
n=int(input())
print(sqrt_binary_search(n))