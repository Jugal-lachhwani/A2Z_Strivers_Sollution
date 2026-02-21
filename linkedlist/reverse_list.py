class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    # Initialize previous pointer to None
    prev = None
    # Start from the head of the list
    temp = head
    # Traverse the list
    while temp:
        # Save the next node
        front = temp.next
        # Reverse the current node's pointer
        temp.next = prev
        # Move prev to current node
        prev = temp
        # Move to the next node
        temp = front
    # Return new head (last node becomes first)
    return prev
