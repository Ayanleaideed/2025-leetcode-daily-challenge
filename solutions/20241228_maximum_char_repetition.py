'''
Problem Description:
The task is to write an algorithm that returns the maximum number of repetitions of a unique character in a given string, composed of English lowercase and uppercase characters. If multiple characters have the same maximum number of repetitions, the character to be returned would be the one that comes first alphabetically with lowercase being given precedence over uppercase.

Solution Approach:
We will use a dictionary to count the frequency of each character. Then, we will iterate over the string in reverse order (to take advantage of python's lexicographical comparison of strings which gives precedence to latter items in the case of a tie). We will keep track of the character with maximum frequency, and if we encounter a character with the same frequency, we compare the characters lexicographically and update our maximum frequency character if necessary.

Complexity Analysis:
- Time: O(n) as we have to iterate over all the characters at least once
- Space: O(n) as in the worst case we might need to create individual entries in the dictionary for each character in the string.
'''

def solution_function(s: str) -> str:
    """
    Given a string s of lowercase and uppercase English characters, 
    returns the maximum number of repetitions of a unique character in s. 
    If there are multiple characters with the same maximum number of repetitions, 
    the function returns the alphabetically earliest character (lowercase is given precedence over uppercase).
    
    Args: 
    s : a string of English alphabets (both lowercase and uppercase) (1 <= len(s) <= 10^5).
    
    Returns:
    A single character string that represents the maximum repeating characters with lowercase precedence.
    """
    # Create a dictionary to count the frequency of characters
    freq = {}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char] = 1
            
    # The character with maximum frequency 
    max_char = max(freq, key=lambda key: (-freq[key], key))
    
    return max_char