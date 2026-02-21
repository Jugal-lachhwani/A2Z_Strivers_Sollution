class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        newHead = self.reverseList(head.next)
        front = head.next
        front.next = head
        head.next = None
        return newHead
    
    def middle_node(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def length_node(self, head):
        length = 0
        while head and head.next:
            length += 1
            head = head.next
        return length + 1
    
    def check_palindrome(self, head):
        middle = self.middle_node(head)
        reversed = self.reverseList(middle.next)
        while reversed:
            if head.val != reversed.val:
                return False
            reversed = reversed.next
            head = head.next
        return True


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(1)

    sol = Solution()
    print(sol.check_palindrome(head))
