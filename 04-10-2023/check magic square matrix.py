##GIVEN MATRIX IS SQUARE MATRIX OR NOT
#input: 2 7 6
#       9 5 1
#       4 3 8
#output:True
def is_magic_square(l):
    n=len(l)
    d1=0
    d2=0
    for i in range(n):
        d1+=l[i][i]
        d2+=l[i][n-i-1]
    if not (d1==d2):
        return False
    for i in range(n):
        sumr=0
        sumc=0
        for j in range(n):
            sumr+=l[i][j]
            sumc+=l[j][i]
        if not (sumr==sumc==d1):
            return False
    return True
mat=[]
for i in range(3):
    row=list(map(int,input().split()))
    mat.append(row)
print(is_magic_square(mat))