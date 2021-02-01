# You are given a singly linked list and an integer k. Return the linked list,
# removing the k-th last element from the list.
#
# Try to do it in a single pass and using constant space.

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)

def remove_kth_from_linked_list(head, k):
    dummy = Node(None, head)
    first = dummy
    prev = dummy

    for i in range(0, k + 1):
        first = first.next

    while first is not None:
        first = first.next
        prev = prev.next

    prev.next = prev.next.next

    return dummy.next

head = Node(1)
print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 1)
print(head)
# [1, 2, 4, 5]