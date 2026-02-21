class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.carry = 0
        
    def getDifference(self, head1, head2):
        len1, len2 = 0, 0
        while head1 or head2:
            if head1:
                len1 += 1
                head1 = head1.next
            if head2:
                len2 += 1
                head2 = head2.next
        return len1 - len2
    
    def addTwoNumbershelper(self, head1, head2):
        while not head1 and not head2:
            return
        self.addTwoNumbershelper(head1.next, head2.next)
        
        sum = head1.val + head2.val + self.carry
        
        if sum < 9:
            self.carry = 0
            head1.val = sum
            return
        else:
            self.carry = sum // 10
            head1.val = sum % 10
            return
                
    def addTwoNumbers(self, l1, l2):
        head1 = l1
        head2 = l2
        nodeh = None
        node = None
        diff = self.getDifference(head1, head2)
        while diff != 0:
            if diff < 0:
                shorter = True
                diff += 1
                head2 = head2.next
            else:
                shorter = False
                diff -= 1
                head1 = head1.next
            if not node:
                node = ListNode(0)
                nodeh = node
            else:
                node.next = ListNode(0)
                node = node.next
        
        if nodeh:
            if shorter:
                node.next = l1
                l1 = nodeh
            else:
                node.next = l2
                l2 = nodeh
            
        self.addTwoNumbershelper(l1, l2)
        
        if self.carry == 0:
            return l1
        else:
            extra = ListNode(self.carry)
            extra.next = l1
            return extra


def create_list(arr):
    head = ListNode(arr[0])
    temp = head
    for i in arr[1:]:
        temp.next = ListNode(i)
        temp = temp.next
    return head


def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next


if __name__ == "__main__":
    num1 = [9, 9, 9, 9, 9]
    num2 = [9, 9, 9, 9, 9]
    l1 = create_list(num1)
    l2 = create_list(num2)

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print_list(result)
