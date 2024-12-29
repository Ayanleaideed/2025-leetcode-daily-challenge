#Author: Ayanle 
#Data: Datetime.now()



'''
Problem Description:
You are given an array of n unique integers that is sorted in ascending order. However, the array has been circularly shifted (all elements are rotated to the right or to the left) an unknown number of times. Your task is to find whether the target element is present in the array or not. If it is present return the index of that element otherwise return -1.

Solution Approach:
The approach to solving this problem is using a modified Binary Search Algorithm. 

First, we find the pivot element( the smallest element) in the array using binary search. The pivot element is the only element for which the next element to it is greater than it. 

After the pivot is found, we do a standard binary search. If the target is greater than the first element, we search in the left half else if the target is less than the first element, we search in the right half.

Complexity Analysis:
- Time: O(logn) : As binary search reduces the search space by half at each step.
- Space: O(1): Since we only create a constant number of variables and don't use any extra space that scales with the input size.

'''

def shiftedArraySearch(nums, target):
    """
    Function to search a target value in a rotated sorted array. 
    Returns the index if target exists, else return -1
    Args: 
    nums(List[int]): Input array of integers
    target(int): Target integer to search in the rotated array

    Returns: 
    int: Index of the target. Returns -1 if target is not in the list
    """
    # Finding the pivot
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    pivot = low

    # Normal Binary Search
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        realMid = (mid + pivot) % len(nums)
        
        if nums[realMid] == target:
            return realMid
        elif nums[realMid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1  # Return -1 if the element is not found in the array
