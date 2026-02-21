class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def delete_Nth_node(self, head, n):
        if not head:
            return
        if n == 1:
            return head.next
        
        temp = head
        while temp and n > 2:
            temp = temp.next
            n -= 1
        temp.next = temp.next.next
        return head


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(7)
    head.next.next.next.next = ListNode(9)

    sol = Solution()
    reversed_head = sol.delete_Nth_node(head, 5)

    while reversed_head:
        print(reversed_head.val, end=" ")
        reversed_head = reversed_head.next
