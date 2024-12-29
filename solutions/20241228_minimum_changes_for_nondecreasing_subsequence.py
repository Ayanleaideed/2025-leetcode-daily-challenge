'''
Problem Description:
The problem asks to find the minimum number of changes required to get a non-decreasing subsequence of size k from an array list (nums).

Solution Approach:
We can solve this problem using dynamic programming. We initialize an array dp of size equal to the array nums' length + 1 and initialize each index to a large value (Infinity).

Starting from the first element of the array list, we find the position (using a binary search) at which the current element can be placed in the dp array such that it is the largest element in a non-decreasing subsequence of the maximum size possible till now.

We then continue the process for each element in the nums.

Finally, we return the difference between k and the maximum size of non-decreasing subsequence in dp array. This shows the minimum number of modifications required.

Complexity Analysis:
- Time: O(n log n), where n is the size of the given nums.
- Space: O(n), where n is the size of the given nums. We use one-dimensional dp array as extra space.

'''

import bisect

def min_changes(nums, k):
    """
    Function to find the minimum number of changes in 'nums' to obtain a non-decreasing subsequence of length 'k'. 
    Args: 
    nums: list of integers
    k: integer, length of the desired subsequence
    Returns: 
    The minimum number of changes required.
    """
    
    dp = [float('inf')] * len(nums)

    for i in range(len(nums)):
        dp[bisect.bisect_left(dp, nums[i])] = nums[i]

    l = bisect.bisect_left(dp, float('inf'))
    return max(0, k - l)
