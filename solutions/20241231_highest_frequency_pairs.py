'''
Problem Description:
Given an array of integers, the task is to find the pair of integers that occur with the highest frequency. If there are multiple such pairs, all such pairs should be returned. The array equally consists of at least 2 different integers and the length of input array could be up to 500.

Solution Approach:
First, calculate the frequency of each integer occurring in the array by using a dictionary where the key is the integer and value is the frequency of the integer in the array. Then, find the maximum frequency among the calculated frequencies. Finally, find the integers that have the maximum frequency and form a pair with themselves and return those pairs in ascending order. To get the pairs in ascending order, the integers are sorted first.

Complexity Analysis:
- Time: O(n logn)
- Space: O(n)

'''

def highest_frequency_pairs(nums):
    """
    Function to find pairs of integers with highest frequency in a given array.
    Args: 
    nums: list of integers where 2 <= len(nums) <= 500
    Returns: 
    List of pairs of integers with the highest frequency, in ascending order.
    """
    # Compute the frequency of each integer
    frequency_dict = {}
    for num in nums:
        if num not in frequency_dict:
            frequency_dict[num] = 1
        else:
            frequency_dict[num] += 1

    # Find the max frequency
    max_frequency = max(frequency_dict.values())

    # Find the integers with max frequency and form pairs
    result = []
    for num, freq in frequency_dict.items():
        if freq == max_frequency:
            result.append([num, num])

    # Return the result in ascending order
    result.sort()
    return result