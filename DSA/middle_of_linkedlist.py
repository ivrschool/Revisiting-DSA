# if two middle return the 2nd
def middleLinkedlist2nd(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data