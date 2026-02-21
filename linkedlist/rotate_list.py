class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def rotateList(head, k):
    if not head:
        return
    
    temp = head
    l = 1
    while temp.next:
        temp = temp.next
        l += 1
    last = temp
    
    if l == k or k == 0:
        return head
    
    n = l - k
    temp = head
    if n == 0:
        return head
    while n > 1:
        temp = temp.next
        n -= 1
    
    newhead = temp.next
    temp.next = None
    last.next = head
    
    return newhead


def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head = rotateList(head, 5)
    printList(head)
