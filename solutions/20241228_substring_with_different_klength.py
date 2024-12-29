'''
Problem Description:
The problem is asking to find all unique substrings that are exactly of length 'k' from the given string 's'. Here, "Unique" means no characters inside the substring are repeated. If there is no possible unique 'k'-length substring, return an empty list.

Solution Approach:
We can solve the problem using the sliding window technique. The sliding window is 'k'. We iterate through the string 's'. In each iteration, we do the following steps:
1. Check if the character already exists in the substring, if it exists, then move the starting pointer to the next character, else:
2. Add the character to the substring.
3. If the length of the substring equals 'k', then:
    i. Add the substring to the result list,
    ii. Move the starting pointer to the next character and remove the character at the starting pointer from the substring.

Complexity Analysis:
- Time: The time complexity is O(n), where n is the length of the input string 's'. We visit each character of the string once.
- Space: The space complexity is O(k), where k is the given integer. In the worst case, we store 'k' characters in the substring.
'''

from collections import deque

def find_unique_substrings(s:str, k:int) -> list[str]:
    """
    This function generates a list of substrings of length 'k' from the given string 's'.
    Here, a substring is unique if all of its characters are distinct.
    Args: 
    s: input string consisting of only ASCII characters.
    k: a non-negative integer less than or equal to the length of the string, length of the substrings to be created.
    Returns: 
    A list of all maximum length unique k-length substrings. An empty list, if there is no possible unique k-length substring.
    """
    substring = deque()
    result = []
    for i in range(len(s)):
        while s[i] in substring:
            substring.popleft()
        substring.append(s[i])
        if len(substring) == k:
            result.append("".join(substring))
            substring.popleft()
    return result

s = "leetcodeproblem"
k = 5
print(find_unique_substrings(s, k))  # ["leetc", "eetcod", "etcodp", "tcodpr", "codpro", "odprob", "dprobl", "proble", "roblem"]