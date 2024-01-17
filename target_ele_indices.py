'''You are given a 0-indexed array nums and a target ele tar .A tar index is an index i such that nums[i]== tar.
Return a list  of tar indies of nums in non-decreasing order.
If there are no tar indices return empty list. The returned list must be in increasing order'''

def quick_sort(arr):  # for sorting we are using quick sort whose Time Complexity is O(nlogn)
     if len(arr) <= 1:
        return arr
     pivot = arr[len(arr) // 2]  # choosing mid ele as pivot 
     left = [x for x in arr if x < pivot]  # left consists of eles < pivot
     middle = [x for x in arr if x == pivot]
     right = [x for x in arr if x > pivot]  # right consists of ele > pivot 
     return quick_sort(left) + middle + quick_sort(right)   #recursively calling quick sort

def find_indices(nums,tar): # finding target indices Time complexity is O(n)
    res_arrr=[]
    for i in range(len(nums)):
        if nums[i]==tar:
            res_arrr.append(i)  # appending tar ele indices 
    return res_arrr        

nums=[2,8,3,20,6,31,8,37]
tar=8
nums=quick_sort(nums)
print(find_indices(nums,tar))


# Timecomplexity ---> O(nlogn)+O(n)--->O(n)



