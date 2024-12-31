#Author: Ayanle A 
#Date: 12/31/2024

'''
Problem Description:
The problem is to determine the minimum possible absolute difference between the sums of the strength levels of the winning and losing players. We are given an array of integers representing the strength of each player. Three important constraints are that all strength values are unique and the total number of players and their strength sums are even.

Solution Approach:
The algorithm involves arranging the players in pairs such that each pair consists of two players with the nearest strength levels. This approach would ensure that the difference of strength level in each pair is minimized, hence, minimizing the overall difference between the sums of the strengths of the winning and losing players. 
So, we first sort the array of strengths. We then loop through the array, summing alternate values as we go along. This way, the first sum will represent the losing players' total strength, and the second will represent the winning players' total strength. 
Lastly, we return the absolute difference between the two sums.

Complexity Analysis:
- Time: O(n log n) due to the sorting of the array, where n is the number of players.
- Space: O(1) as no additional space is needed except the input array and variables to store the sums.
'''

def pairwiseGame(arr):
    """
    Returns the minimum absolute difference between the sums of the strengths
    of the winning and losing players.
    Args:
        arr: A list of integers representing the strength levels of the players.
    Returns: An integer representing the minimum absolute difference.
    """
    # Sorting the array
    arr.sort()

    # Initialising the sums of the strengths of the winning and losing players
    win_sum, lose_sum = 0, 0
    
    # Looping through the array
    for i in range(len(arr)):
        if i % 2 == 0:
            lose_sum += arr[i]
        else:
            win_sum += arr[i]

    # Returning the absolute difference 
    return abs(win_sum - lose_sum)
