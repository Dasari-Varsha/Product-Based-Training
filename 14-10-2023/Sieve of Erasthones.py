#Sieve of Erasthones
def sieve_of_erasthones(num):
    prime=[True for i in range(num+1)]
    p=2
    count=0
    while p*p<=num:
        if prime[p]:
            for i in range(p*p,num,p):
                prime[i]=False
        p+=1
    for p in range(2,num):
        if prime[p]:
            print(p)
            count+=1
    print("No.of primes::",count)
num=int(input())
sieve_of_erasthones(num)