# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# function to find large sum
def maxSubArray(nums):
        if len(nums) == 1: # for one ele in nums
            return nums[0]
        far=end=nums[0] 
        for i in range(1,len(nums)): # Time Complexity --- O(N)
            end=max(nums[i],end+nums[i]) # for current sum
            far=max(far,end) # for largest sum
        return far                

arr=[1,2,3,-1,1,2,3]
print(maxSubArray(arr))

# Time Complexity --- O(N) where N is the length of nums
# Space Complexity --- O(1)