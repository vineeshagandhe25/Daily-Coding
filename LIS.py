''' Question: Given an array of integers, find the longest increasing subsequence (LIS). A subsequence is a sequence that can be derived from an array
 by deleting some or no elements without changing the order of the remaining elements.
   For example, [3, 4, 5, 1, 9] is a subsequence of [3, 1, 4, 1,5,9,2,6,5].'''

# function to find longest increasing subsequence (LIS)
def LIS(nums):
    length=len(nums)
    dp=[1]*length
    for i in range(1,length):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i]=max(dp[i],dp[j]+1)

    return max(dp)
nums=[3, 1, 4, 1,5,9,2,6,5]
print(LIS(nums))          
                    
            