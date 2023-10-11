#check Palindrome or not
str1=input()
rev=str1[::-1]
if rev==str1:
    print("palindrome")
else:
    print("not palindrome")
   OR
str1=input("Enter the string:")
i=0
j=len(str1)-1
while(i<j):
    if(str1[i]!=str1[j]):
        print("Not palindrome")
        break
    i+=1
    j-=1
else:
    print("Palindrome")
    
    
#Palindrome with recursion
def fun(s,i,j):
    if i>j:
        return True
    if s[i]!=s[j]:
        return False
    return fun(s,i+1,j-1)
s=input("Enter the string:")
print(fun(s,0,len(s)-1))