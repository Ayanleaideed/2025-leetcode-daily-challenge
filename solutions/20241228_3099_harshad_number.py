#Author: Ayanle 
#Data: Datetime.now()


'''
Problem Description:
We are given an integer 'x'. If 'x' is divisible by the sum of its digits, it is considered to be a Harshad number. Our task is to return the sum of the digits of 'x' if 'x' is a Harshad number, otherwise, return -1.

Solution Approach:
The core algorithm starts by converting the given integer 'x' into its Digit representation. Then, the sum of its digits is computed. If the given integer is divisible by the sum of its digits, return the sum of the digits. Otherwise, return -1.

Complexity Analysis:
- Time: O(n), where n is the number of digits in integer 'x'.
- Space: O(1), since we're using only a constant amount of space.

'''

def is_harshad(x):
    """
    Returns the sum of the digits of x if x is a Harshad number, otherwise -1.
    
    Args:
    x: An integer value which is to be tested if it's a Harshad number or not.

    Returns: 
    The sum of the digits of x if x is a Harshad number, otherwise returns -1.
    """
    # Convert x to string to get the digits
    digit_str = str(x)
    
    # Calculate the sum of digits
    digit_sum = sum(int(d) for d in digit_str)
    
    # Check if x is divisible by the sum of its digits, if yes return the sum else return -1
    return digit_sum if x % digit_sum == 0 else -1
