class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def mergeTwoSortedList(self, left, right):
        temp = None
        temph = None
        
        while left or right:
            if not left:
                if not temp:
                    temp = right
                    temph = temp
                else:
                    temp.next = right
                    temp = temp.next
                right = right.next
            elif not right:
                if not temp:
                    temp = left
                    temph = temp
                else:
                    temp.next = left
                    temp = temp.next
                left = left.next
            elif left.val > right.val:
                if not temp:
                    temp = right
                    temph = temp
                else:
                    temp.next = right
                    temp = temp.next
                right = right.next
            else:
                if not temp:
                    temp = left
                    temph = temp
                else:
                    temp.next = left
                    temp = temp.next
                left = left.next
            
        return temph           
    
    def middle_node(self, head):
        slow = head
        fast = head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        middle = self.middle_node(head)
        right = middle.next
        middle.next = None
        left = head
        left = self.sortList(left)
        right = self.sortList(right)
        
        return self.mergeTwoSortedList(left, right)


if __name__ == "__main__":
    head2 = ListNode(1)
    head2.next = ListNode(4)
    head2.next.next = ListNode(2)
    head2.next.next.next = ListNode(6)
    head2.next.next.next.next = ListNode(8)

    sol = Solution()
    reversed_head = sol.sortList(head2)

    while reversed_head:
        print(reversed_head.val, end=" ")
        reversed_head = reversed_head.next
