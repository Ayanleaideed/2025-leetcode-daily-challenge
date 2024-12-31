'''
Problem Description:
Given two integer arrays representing schedules of passenger arrivals and departures, the task is to determine the minimum number of buses required by a company to operate for the night under the constraint that every group of passengers arrives at their destination by their departure time and that no bus carries more than one group at a time.

Solution Approach:
Our approach will be to first sort the intervals (arrival, departure) in ascending order of arrival time and then iterate over the intervals. Pointers will track the current bus and next group of passengers. This algorithm is akin to the interval scheduling problem and efficient due to its greedy approach.

Complexity Analysis:
- Time: O(n log(n)) where n is number of groups, due to sorting of intervals.
- Space: O(n) for storing the intervals and heap based data structure. 
'''

from typing import List
import heapq

def minimumBuses(arrivals: List[int], departures: List[int]) -> int:
    """
    Returns the minimum number of buses that the company will need.
    
    Args: 
    arrivals: A List of integers representing the arrival times of the passengers.
    departures: A List of integers representing the departure times of the passengers.
        
    Returns:
    An integer representing the minimum number of buses needed.
    """

    # create list of tuples (arrival, departure)
    intervals = sorted(zip(arrivals, departures))

    # initialize heap with first departure time
    heap = [intervals[0][1]]

    for i in range(1, len(intervals)):
        if intervals[i][0] > heap[0]:
            # if the arrival time of next group is after the departure time of the group in current bus
            # replace the departure time of the group in the bus with the current group
            heapq.heapreplace(heap, intervals[i][1])
        else:
            # if the arrival time of next group is before the departure time of the group in current bus
            # allocate a new bus for the current group
            heapq.heappush(heap, intervals[i][1])

    # number of buses needed is equal to the size of the heap
    return len(heap)