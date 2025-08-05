#1.0 reverse a linked list

from DSA.revisiting_linked_list_1 import ListNode, reverseListRecursion,reverseListIterative, cloneList, printList

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:


# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []
 

# test examples with iterative approach

#Example 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

# Clone before reversing
original_linked_list = cloneList(head)

# Reverse
reversed_linked_list = reverseListIterative(head)

print("Original list:")
printList(original_linked_list)

print("Reversed list:")
printList(reversed_linked_list)



# test examples with iterative approach

#Example 2
head = ListNode(1)
head.next = ListNode(2)

# Clone before reversing
original_linked_list = cloneList(head)

# Reverse
reversed_linked_list = reverseListIterative(head)

print("Original list:")
printList(original_linked_list)

print("Reversed list:")
printList(reversed_linked_list)




# test examples with recursive approach

#Example 1
head = ListNode()

# Clone before reversing
original_linked_list = cloneList(head)

# Reverse
reversed_linked_list = reverseListIterative(head)

print("Original list:")
printList(original_linked_list)

print("Reversed list:")
printList(reversed_linked_list)







