class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class Solution:
    def segregate_odd_even(self, head):
        if not head:
            return
        even1 = None
        odd1 = None
        temp = head
        odd = None
        even = None
        while temp:
            if temp.val % 2 == 0:
                if even:
                    even.next = temp
                    even = even.next
                else:
                    even = temp
                    even1 = even
            else:
                if odd:
                    odd.next = temp
                    odd = odd.next
                else:
                    odd = temp
                    odd1 = odd
            temp = temp.next
        
        if not even1:
            return odd1
        if not odd1:
            return even1
        
        even.next = odd1
        return even1


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(3)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(7)
    head.next.next.next.next = ListNode(9)

    sol = Solution()
    reversed_head = sol.segregate_odd_even(head)

    while reversed_head:
        print(reversed_head.val, end=" ")
        reversed_head = reversed_head.next
