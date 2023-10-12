#75. Sort Colors
#Example 1:
#Input: nums = [2,0,2,1,1,0]
#Output: [0,0,1,1,2,2]
#using 3-pointer algorithm
nums=list(map(int,input().split()))
i=0
l=0
r=len(nums)-1
while i<=r:
    if nums[i]==0:
        nums[i],nums[l]=nums[l],nums[i]
        l+=1
        i+=1
    elif nums[i]==1:
        i+=1
    elif nums[i]==2:
        nums[i],nums[r]=nums[r],nums[i]
        r-=1
print(nums)

#USING COUNTING SORT
nums=list(map(int,input().split()))
count=[0 for i in range(len(nums))]
for i in range(len(nums)):
    count[nums[i]]+=1
for i in range(1,len(count)):
    count[i]+=count[i-1]
res=[0]*len(nums)
for i in range(len(nums)):
    res[count[nums[i]]-1]=nums[i]
    count[nums[i]]-=1
print(res)
