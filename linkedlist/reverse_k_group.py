class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while True:
            kth = self.getKthNode(groupPrev, k)
            if not kth:
                break

            groupNext = kth.next

            # Reverse the current k nodes
            prev = groupNext
            curr = groupPrev.next

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect the reversed group to the previous part
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next

    def getKthNode(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


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

    k = 3
    sol = Solution()
    result = sol.reverseKGroup(head, k)
    printList(result)
