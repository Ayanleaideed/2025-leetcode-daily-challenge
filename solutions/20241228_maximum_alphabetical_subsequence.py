Problem Description:
Given a string 's', we need to find the longest subsequence so that all characters of the subsequence are sorted in alphabetical order. A subsequence does not need to be contiguous, and there can be multiple correct answers but we need to return one which longest.


Solution Approach:
We can view this problem as the classic problem of finding the Longest Increasing Sub-sequence (LIS) where the sequence is the UTF-16 values of characters in the string 's'.

The Dynamic Programming (DP) algorithm for the LIS problem is suitable here. We start from the first character and find the longest sub-sequence for substring ending at that character. We repeat the same for all characters.

Then, we go through the DP table to find the maximum length (i.e., the length of the longest alphabetical sequence) and the location at which it ends. We then retrace our steps backwards from this location in the DP table and the UTF-16 values table while the length is greater than 0.


Complexity Analysis:
- Time: O(N^2)
- Space: O(N)

```python
def max_alpha_subsequence(s: str) -> str:
    """
    Given a string s, find the longest alphabetical subsequence.
    Args: s: str: input string (1 <= len(str) <= 10000)
    Returns: str: longest alphabetical subsequence
    """

    n = len(s)
    dp = [1] * n 
    for i in range (1 , n):
        for j in range(i):
            if ord(s[j]) <= ord(s[i]):
                dp[i] = max(dp[i], dp[j]+1)
                
    maxlen = max(dp)
    idx = dp.index(maxlen)
    result = [chr(ord(s[idx]))]
    for i in range(idx-1, -1, -1):
        if dp[i] == maxlen-1 and ord(s[i]) <= ord(result[-1]):
            result.append(s[i])
            maxlen -= 1
    return ''.join(result[::-1])
```
This solution function returns the longest alphabetical subsequence in the given string 's'. Two dynamic programming tables (dp, used to keep tab of the longest subsequence ending at each index, and result, used to build the longest sequence) are built first. The longest alphabetical subsequences are extracted from the dp and result tables. These subsequences are then joined to form the final result which is returned by the function.