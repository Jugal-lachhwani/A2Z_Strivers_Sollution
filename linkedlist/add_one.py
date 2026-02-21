class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def __init__(self):
        self.num = True
        
    def add_one_helper(self, head):
        if not head:
            return
        self.add_one_helper(head.next)
        
        if self.num:
            if head.val < 9:
                head.val += self.num
                self.num = False
            else:
                head.val = 0
        
    def add_one(self, head):
        if not head:
            return
        
        self.add_one_helper(head)
        
        if self.num == False:
            return head
        else:
            extra = ListNode(1)
            extra.next = head
            return extra


if __name__ == "__main__":
    head2 = ListNode(9)
    head2.next = ListNode(9)
    head2.next.next = ListNode(9)
    head2.next.next.next = ListNode(9)
    head2.next.next.next.next = ListNode(9)

    sol = Solution()
    reversed_head = sol.add_one(head2)

    while reversed_head:
        print(reversed_head.val, end=" ")
        reversed_head = reversed_head.next
