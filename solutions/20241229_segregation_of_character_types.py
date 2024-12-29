'''
Problem Description:
We have an array of characters consisting of lowercase letters, uppercase letters, and special (non-alphanumeric) characters. The task is to segregate the characters in such a way that all lowercase letters come first, followed by uppercase letters and then the special characters. The order of characters within each group does not matter.

Solution Approach:
We can solve this using the Dutch National Flag Algorithm with a little modification. Instead of just three types (0, 1, 2), we have three types of characters (lowercase, uppercase, special). We initialize three pointers, low, mid and high. We then iterate over the array, when we find a lowercase character, we swap it to the front (low pointer) and move all pointers up. If we find an uppercase character, we leave it where it is (mid pointer) and move the mid pointer up. If we find a special character, we swap it to the end (high pointer) and leave the high pointer where it is. After the end of the iteration, all characters would have been placed at their correct positions.

Complexity Analysis:
- Time: O(n) We need to do a single pass over all elements. Here, n is the length of array.
- Space: O(1) We just use three extra pointers, so the space complexity is constant.

'''

from typing import List

def segregateChar(charArray: List[str]) -> List[str]:
    """
    This function accepts an array of characters consisting of lowercase letters, uppercase letters, 
    and special characters. It then segregates the characters placing all lowercase letters first, 
    followed by uppercase letters and then the special characters.
    Args: 
    charArray (List[str]): The character array.
    Returns: 
    List[str]: The segregated character array.
    """

    def swap(arr: List[str], i: int, j: int):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        
    low = mid = 0
    high = len(charArray) - 1

    while mid <= high:
        if charArray[mid].islower():
            swap(charArray, low, mid)
            low += 1
            mid += 1
        elif charArray[mid].isupper():
            mid += 1
        else:
            swap(charArray, mid, high)
            high -= 1

    return charArray