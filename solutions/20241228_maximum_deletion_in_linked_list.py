'''
Problem Description:
Given a singly linked list, we need to design an algorithm that will remove all instances of a specific integer (x) from the list. The result will be the head of the altered linked list.

Solution Approach:
We can use a "dummy" node at the beginning of our list, which will help us to manage cases when the head node needs to be deleted. We can initialize two pointers, prev and curr, where prev is initialized as the dummy node and curr is initialized as the head of the list. As we traverse the list, we can check each node's value. If the current node's value is not equal to x, we update prev to be the current node. If it is equal to x, we bypass the current node by updating the next pointer of the previous node to point to the current node's next node.

Complexity Analysis:
- Time: O(N), where N represents the number of nodes in the linked list. We basically process each node once.
- Space: O(1), as we are not using any extra space proportional to the input.

'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeElements(head, x):
    """
    Removes all occurrences of a given integer x in the linked list
    Args: 
    head (ListNode): The head of the linked list
    x (int): The integer to be removed from the list

    Returns: ListNode: The head of the altered linked list
    """

    # Create the dummy node and initialize pointers
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        # If the current node's value is not x, then prev moves to the 
        # current node
        if curr.val != x:
            prev = curr
        # If the current node's value is x, then prev's next pointer bypasses 
        # the current node to avoid it
        else:
            prev.next = curr.next
        curr = curr.next

    return dummy.next
