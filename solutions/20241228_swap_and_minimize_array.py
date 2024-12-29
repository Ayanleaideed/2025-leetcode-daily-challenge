#Author: Ayanle 
#Data: Datetime.now()

'''
Problem Description:
You are given an array of integers range from 1 to 100. You are allowed to swap any two elements of the array any number of times. 
The goal is to minimize the sum of the absolute differences of all adjacent pairs in the array.

Solution Approach:
The best approach is to sort the array in ascending order. This will ensure that the sum of the absolute differences of all adjacent pairs is minimized. 
Then, iterate through the array and sum the absolute differences between each pair of adjacent elements.

Complexity Analysis:
- Time: O(nlogn) because sorting the array takes O(nlogn) time. After sorting, we just iterate over the array once, which takes O(n) time.
- Space: O(1) We are not using any extra space that scales with input size, so the space complexity is constant.
'''

def minimizeArray(nums):
    """
    Minimizes the sum of the absolute differences of all adjacent pairs in the array.
    Args: nums: List of integers.
    Returns: Minimum possible sum of the absolute differences of all adjacent pairs in the array.
    """

    # Sorting the array
    nums.sort()

    # Iterating through the array and calculating the sum of 
    # absolute differences between each pair of adjacent elements.
    sum_diff = 0
    for i in range(1, len(nums)):
        sum_diff += abs(nums[i] - nums[i-1])
    
    return sum_diff
```
Usage:

```Python
print(minimizeArray([5, 3, 9, 1, 6]))  # prints 7
print(minimizeArray([1, 1, 1]))  # prints 0
```
