#Author: Ayanle 
#Data: Datetime.now()

'''
Problem Description:
We are to determine a number at a certain position in a Fibonacci-like sequence, given the first two numbers, 'm' and 'n', and the position 'k'. Unlike the common Fibonacci sequence which starts with 0 and 1, this one starts with 'm' and 'n'.

Solution Approach:
First, we initialize a list to store our sequence with 'm' and 'n' being the first two numbers. Afterward, we start a loop from 2 which goes up to 'k'. In each loop iteration, the next number in the sequence is computed by summing up the two preceding numbers and taking modulo of 10^9+7. This number is then added to the list. At the end, we return the 'k'-th element from our sequence.

Complexity Analysis:
- Time: O(k) as we iterate from 2 up to 'k' to fill up our sequence.
- Space: O(k) as we use a list to store our sequence. Note that 'k' could go up to 10^6.

'''

def modifiedFibonacci(m: int, n: int, k: int) -> int:
    """
    Function to compute the 'k'-th number in a Fibonacci-like sequence
    Args: 
    m: first number in the sequence
    n: second number in the sequence
    k: position in the sequence
    Returns: 'k'-th number in the sequence
    """
    # Initialize a list to store the sequence
    sequence = [0] * k
    sequence[0] = m
    sequence[1] = n

    # Fill up the sequence
    for i in range(2, k):
        sequence[i] = (sequence[i-1] + sequence[i-2]) % (10**9 + 7)

    return sequence[k-1]
