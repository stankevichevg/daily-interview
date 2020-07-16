# Given an integer k and a binary search tree, find the floor (less than or equal to) of k,
# and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.
#
# Here is the definition of a node for the tree.


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def find_ceiling_floor(root_node, k, floor=None, ceil=None):
    if root_node is None:
        return floor, ceil
    elif root_node.value < k:
        return find_ceiling_floor(root_node.right, k, root_node.value, ceil)
    elif root_node.value > k:
        return find_ceiling_floor(root_node.left, k, floor, root_node.value)
    elif root_node.value == k:
        if root_node.left is not None and root_node.right is not None:
            return root_node.left.value, root_node.right.value
        elif root_node.left is not None:
            return root_node.left.value, ceil
        elif root_node.right is not None:
            return floor, root_node.right.value


root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(find_ceiling_floor(root, 5))
# (4, 6)