# This problem was recently asked by Microsoft:
#
# You are given two linked-lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        cur_l1 = l1
        cur_l2 = l2
        mem = 0
        result = ListNode(0)
        cur_result = result
        while True:
            cur_l1_value = cur_l1.val if cur_l1 is not None else 0
            cur_l2_value = cur_l2.val if cur_l2 is not None else 0
            sum = cur_l1_value + cur_l2_value + mem
            mem = (int) (sum / 10)
            value = sum % 10
            cur_l1 = cur_l1.next if cur_l1 is not None else None
            cur_l2 = cur_l2.next if cur_l2 is not None else None
            cur_result.val = value
            if cur_l1 is None and cur_l2 is None:
                break
            else:
                cur_result.next = ListNode(0)
                cur_result = cur_result.next
        return result


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
