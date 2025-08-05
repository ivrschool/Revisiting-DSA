#iterative approach

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseListIterative(head):
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next  # Save next
        curr.next = prev       # Reverse pointer
        prev = curr            # Move prev forward
        curr = next_node       # Move curr forward
        
    return prev

#recursive approach

def reverseListRecursion(head):
    if not head or not head.next:
        return head

    new_head = reverseListRecursion(head.next)
    head.next.next = head
    head.next = None
    
    return new_head

#helper functions

def printList(head):
    while head:
        print(head.val)
        head = head.next

def cloneList(head):
    if not head:
        return None
    new_head = ListNode(head.val)
    current_old = head.next
    current_new = new_head
    while current_old:
        current_new.next = ListNode(current_old.val)
        current_old = current_old.next
        current_new = current_new.next
    return new_head
