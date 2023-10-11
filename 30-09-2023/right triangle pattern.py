#input:4
#output:*
#       * *
#       * * *
#       * * * *
n=int(input())
for i in range(0,n):
    for j in range(0,i):
        print("*",end=" ")
    print(" ")