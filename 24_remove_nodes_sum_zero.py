# Given a linked list of integers, remove all consecutive nodes that sum up to 0.
#
# Example:
# Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
# Output: 10
#
# The consecutive nodes 5 -> -3 -> -3 -> 1 sums up to 0 so that sequence should be removed.
# 4 -> -4 also sums up to 0 too so that sequence should also be removed.

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def remove_consecutive_sum_to0(node):
    acc = 0
    mem = {acc: Node(0, node)}
    current = node
    while current is not None:
        acc += current.value
        if acc in mem.keys():
            sum = acc
            # delete nodes from mem
            to_delete = mem[acc].next
            while to_delete != current:
                sum += to_delete.value
                del mem[sum]
                to_delete = to_delete.next
            # make new link
            mem[acc].next = current.next
        else:
            mem[acc] = current
        current = current.next
    return mem[0].next


node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)

node = remove_consecutive_sum_to0(node)

while node:
    print(node.value)
    node = node.next
