#tower of hanoi
#no.of moves required to shift n disks to destination
#input:3
#output:7
def tower_of_hanoi(n,src,aux,dest):
    if n==1:
        return 1
    return tower_of_hanoi(n-1,src,dest,aux)+1+tower_of_hanoi(n-1,aux,src,dest)
n=int(input())
src=" "
aux=" "
dest=" "
print(tower_of_hanoi(n,src,aux,dest))
           OR
def TOH(n, src, aux, dest):
    if n == 1:
        print("I moved from "+src+" to " +dest)
        return
    TOH( n-1, src, dest, aux)
    print("I moved from "+src+" to " +dest)
    TOH( n-1, aux, src, dest)
n=int(input())
TOH(n, 'src', 'aux', 'dest')
