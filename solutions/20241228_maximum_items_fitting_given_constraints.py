#Author: Ayanle 
#Data: Datetime.now()


'''
Problem Description:
In this problem, we are given an array of integers 'items' which represents the size of each item and two integer values 'limit1' and 'limit2' which represent the carrying capacity of two sacks. Our task is to determine the maximum number of items we can fit into the sacks without exceeding their carrying limits. 

Solution Approach:
We can solve this problem by sorting the items in increasing order, next, we will use two index pointers one from the start and another from the end. At each step, we decide to put the bigger item into the sack which is currently capable of holding more weight. If one sack is full we continue placing in the other until we are done or both sacks can't hold any more items.

Complexity Analysis:
- Time: The time complexity is O(n log n) because we have to sort the items first and next we use two pointers to perform linear search.
- Space: The space complexity is O(1) as we are not using any extra space that grows with input size.

'''

from typing import List

def maximumItems(items: List[int], limit1: int, limit2: int) -> int:
    """
    This function takes as input a list of integers representing items sizes and two limits representing the sack capacities.
    It returns the maximum number of items that can be fit into both the sacks within their carrying capacity.
    """
    # Sort the items in increasing order
    items.sort()
    
    # Initialize two pointers. One at the beginning and the other at the end.
    i, j = 0, len(items)-1
    
    # Initialize the count of items that can be put into the sacks.
    count = 0
    
    while i <= j:
        # If the item at the end of the list can fit into the sack with larger remaining capacity, put it there.
        if max(limit1, limit2) >= items[j]:
            if limit1 > limit2:
                limit1 -= items[j]
            else:
                limit2 -= items[j]
            j -= 1
        # If it cannot, then try to put the item at the start of the list into the sack with smaller remaining capacity.
        elif min(limit1, limit2) >= items[i]:
            if limit1 < limit2:
                limit1 -= items[i]
            else:
                limit2 -= items[i]
            i += 1
        # If neither item can fit into either sack, we cannot put any more items into the sacks.
        else:
            break
        
        # Increase the count of items that can be put into the sacks.
        count += 1
    
    return count
