#Author: Ayanle 
#Data: Datetime.now()



'''
Problem Description:
We are given an array of strings, i.e. the list of words. The task is to find the longest word from this list such that it contains non-repeating characters. If there are multiple such words, return the one that appears first in the list.

Solution Approach:
For this problem, we can make use of a HashSet to record the occurrence of each character in the words. The use of HashSet allows us to quickly check if a character has duplicated in a word(one on one time complexity for HashSet element search). We traverse the array from the beginning and keep track of the longest word with unique characters encountered so far. If we encounter a longer word with unique characters, we update our answer.

Complexity Analysis:
- Time Complexity: O(n), where n is the total number of characters in all words, because we are traversing all the characters once.
- Space Complexity: O(1), because the extra space used by the HashSet does not change with the increase in input size, as there are only 26 lowercase alphabets.

'''

from typing import List

def longest_non_repeating_substring(wordList: List[str]) -> str:
    """
    Returns the first longest word with non-repeating characters from the list of words.
    Args:
    wordList : List : a list of n words composed of lowercase alphabets.

    Returns:
    str : the first longest word with unique characters. Returns empty string if no such word is found.
    """
    longest_word = ''
    for word in wordList:
        if len(set(word))==len(word) and len(word)>len(longest_word):
            longest_word = word
    return longest_word
