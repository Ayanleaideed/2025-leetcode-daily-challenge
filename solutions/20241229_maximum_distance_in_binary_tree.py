#Author: Ayanle 
#Data: Datetime.now()



'''
Problem Description:
Given a binary tree, your task is to find the maximum distance between two different tree nodes. The distance between two nodes is the number of edges along the shortest path from one node to another.

Solution Approach:
The maximum distance could be the diameter of the tree which is the largest distance between two leaf nodes. It either passes through the root or doesn't pass through the root. To find the maximum diameter, we compute the maximum depth for both left and right subtree and keep track of the maximum diameter found so far. The maximum diameter would be the larger of the maximum diameter found so far and the sum of max depth from left and right subtree.

Complexity Analysis:
- Time: O(N) where N is the total number of nodes in the tree.
- Space: O(H) where H is the height of the tree due to the recursion stack.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def maxDistance(root):
    """
    Function to find maximum distance between two nodes in a binary tree.
    Args: 
    root(TreeNode): Root node of the binary tree.
    Returns: 
    int: Maximum distance between any two given nodes
    """
    # Initialization
    self.maxDiameter = 0
    
    def depth(node):
        if node is None:
            return 0

        # compute depth on both left and right subtree recursively
        left = depth(node.left)
        right = depth(node.right)
        
        # calculate current diameter as the sum of depths from left and right subtree
        # and update the maximum diameter if current diameter is larger
        self.maxDiameter = max(self.maxDiameter, left + right)
        
        # return maximum depth from left and right subtree
        return max(left, right) + 1

    depth(root)
    # return the maximum distance
    return self.maxDiameter
