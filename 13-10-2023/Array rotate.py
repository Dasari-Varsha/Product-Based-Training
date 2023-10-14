#ARRAY ROTATE
nums=[1,2,3,4,5,6,7]
k=3
temp=[]
for i in range(k+1,len(nums)):
    temp.append(nums[i])
for i in range(0,k):
    temp.append(nums[i])
nums[:]=temp
print(nums)
OR
n=len(nums)-k
nums[:]=nums[n:]+nums[:n]