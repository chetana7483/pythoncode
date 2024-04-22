nums=[12,34,2,56,90,33,89,120,20,25,191]
target=25
nums=sorted(nums)
left=0
right=len(nums)-1
found=False

while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        found=True
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid+1
if found==True:
    print("element is found in the list",target)
else:
    print("element is not found in the list") 
#complexities order (time as well as space)              
#o(1)<o(log N)<o(sgrt N)<o(N)<o(N log N)<o(N^N)<o(N^N*N)<...
