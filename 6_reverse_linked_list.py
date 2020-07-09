# Given a singly-linked list, reverse the list. This can be done iteratively or recursively.
# Can you get both solutions?
#
# Example:
# Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
# Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def print_list(self):
        node = self
        output = ''
        while node is not None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    def reverse_iteratively(self, head):
        result = head
        tail = head.next
        result.next = None
        while tail is not None:
            tail_top = tail
            tail = tail.next
            tail_top.next = result
            result = tail_top
        return result

    def reverse_recursively(self, head):
        def reverse(list_head):
            if list_head.next is None:
                return list_head, list_head
            else:
                top = list_head
                tail = list_head.next
                top.next = None
                first, last = reverse(tail)
                last.next = top
                return first, top
        return reverse(head)[0]


# Test Program
# Initialize the test list:
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.print_list()
# 4 3 2 1 0
testHead.reverse_iteratively(testHead)
# testHead.reverse_recursively(testHead)
print("List after reversal: ")
testTail.print_list()
# 0 1 2 3 4