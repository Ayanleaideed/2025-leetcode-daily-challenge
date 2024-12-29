#Author: Ayanle 
#Data: Datetime.now()


'''
Problem Description:
The problem is asking to find the sum of elements of the subarrays which are multiples of the input k from the integer array `arr`.

Solution Approach:
A prefix sum approach will be used to solve this problem. The prefix sum array tracks the sum of all elements that were before a given index. For every index in the prefix sum array, the resulting element will be the sum of the current element and previous prefix sum value. The modulo of the prefix sum array is taken with respect to 'k' at each point, storing these occurrences in a count map. Then, for each unique modulo result, calculate and add the possible subarray combinations to the total count. The count map is updated throughout the process. 

In the end, the total count will contain the sum of all elements in the subarrays of `arr` that are multiples of `k`. 

Complexity Analysis:
- Time: O(n) - Iterating through the array only once, where 'n' is the size of the array.
- Space: O(n) - Storing prefix sums and their count in a map/dictionary.
'''

def sumOfSubarrayMultiples(arr, k):
    """
    Solve the sum of subarray multiples problem using prefix sum approach.
    Args: 
    arr (list): input array of integers
    k (int): integer to find the multiples of
    Returns: 
    int: the sum of all elements in the subarrays of arr that are multiples of k.
    """
    n = len(arr)
    mod = [0]*k
    prefix_sum = 0
    total = 0
    
    # Create prefix sum array and update count of mod k prefix sums
    for i in range(0,n):
        prefix_sum = (prefix_sum + arr[i]) % k
        mod[prefix_sum] += 1
        
    # Calculate total sum of subarray elements
    for i in range(0,k):
        if mod[i] > 1:
            total += (mod[i]*(mod[i]-1)) // 2
            
    # Adding the elements which are individually divisible by 'k'
    total += mod[0]
    
    return total
