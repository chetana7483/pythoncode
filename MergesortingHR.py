def mergeTwoArrays(left, mid, right, nums):
    index1 = left
    index2 = mid + 1 
    temp = []
 
    while index1 <= mid and index2 <= right:
        if nums[index1] > nums[index2]:
            temp.append(nums[index2])
            index2 += 1 
        else:
            temp.append(nums[index1])
            index1 += 1 
 
    while index1 <= mid:
        temp.append(nums[index1])
        index1 += 1 
 
 
    while index2 <= right:
        temp.append(nums[index2])
        index2 += 1 
 
    curr = 0
    for position in range(left, right + 1):
        nums[position] = temp[curr]
        curr += 1 
 
 
def divideIt(left, right, nums):
    if left >= right:
        return
 
    mid = (left + right) // 2
    divideIt(left, mid, nums)
    divideIt(mid + 1, right, nums)
    mergeTwoArrays(left, mid, right, nums)
n=int(input())
nums=list(map(int,input().split()))
divideIt(0, len(nums) - 1, nums)
print(*nums)
 
