#Author: Ayanle 
#Data: Datetime.now()



'''
Problem Description:
The problem is to sort an array into a 'Peak Pattern', in which the highest element in the array is at the middle, and the elements decrease symmetrically towards the ends. The condition is that the array should have a unique maximum and an odd number of elements (to have the symmetric decrease on both sides). If it is not possible to form the Peak Pattern, return -1.

Solution Approach:
The approach is to find the max element and its index first. If the max element has valid indices (its indices * 2 + 1 equals to the array's length), we sort the left and right sides of the array using a heap sort algorithm. Heap sort is an efficient sorting algorithm that is suitable for this problem because it uses a binary heap and can sort in place. It provides a time complexity of O(n log(n)) which satisfies the problem's requirement.

Complexity Analysis:
- Time: O(n log(n)) - The time complexity of heap sort is O(n log(n)).
- Space: O(1) - The space complexity is constant because heap sort can sort in place without using additional space.

'''

def solution_function(array):
    """
    Sorts an array into a "Peak Pattern"
    Args: 
        array: A list of integers, where n > 3.
    Returns:
        A list of integers sorted in "Peak Pattern", or -1 if it's not possible.
    """
    
    # Function to do heapify 
    def heapify(arr, n, i): 
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
  
        if left < n and arr[largest] < arr[left]: 
            largest = left
  
        if right < n and arr[largest] < arr[right]: 
            largest = right
  
        if largest != i: 
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest) 

    # Main function to do heap sort 
    def heapSort(arr): 
        n = len(arr) 
  
        for i in range(n, -1, -1): 
            heapify(arr, n, i) 

        for i in range(n-1, 0, -1): 
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0) 
            
    # Getting maximum's index  
    max_i = array.index(max(array))
  
    # check if max's index is valid
    if max_i * 2 + 1 != len(array):
        return -1
  
    # sort left side of max
    heapSort(array[:max_i])
    # sort right side of max
    heapSort(array[max_i + 1:])
  
    return array
