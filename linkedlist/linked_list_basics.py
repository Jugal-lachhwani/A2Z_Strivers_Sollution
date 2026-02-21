class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def insert_back(head, val):
    if not head:
        head = Node(val)
        return head
    
    temp = head
    while temp.next:
        temp = temp.next
    temp.next = Node(val)
    return head


def insert_first(head, val):
    if not head:
        head = Node(val)
        return head
    
    temp = head
    head = Node(val)
    head.next = temp
    return head


def insert_after_pos(head, val, pos):
    if not head:
        head = Node(val)
        return head
    newnode = Node(val)
    temp = head
    
    while temp.next and pos != 1:
        pos -= 1
        temp = temp.next
    
    if temp.next:
        old = temp.next
        temp.next = newnode
        newnode.next = old
        return head
    
    temp.next = newnode
    return head


def delete_node(head, pos):
    if not head:
        return None
    
    if pos == 0:
        head = head.next
        return head
    
    cur_pos = 1
    temp = head
    while temp.next.next:
        if cur_pos == pos:
            temp.next = temp.next.next
            return head
        cur_pos += 1
        temp = temp.next
    return head


def print_list(head):
    if not head:
        return
    temp = head
    while temp.next:
        print(temp.val)
        temp = temp.next
    print(temp.val)


head = insert_back(None, 3)
insert_back(head, 8)
insert_back(head, 18)
insert_back(head, 28)
insert_back(head, 48)
head = delete_node(head, 0)
insert_after_pos(head, 38, 4)
head = insert_first(head, 56)
print_list(head)
