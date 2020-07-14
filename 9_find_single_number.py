# Given a list of numbers, where every number shows up twice except for one number, find that one number.
#
# Example:
# Input: [4, 3, 2, 4, 1, 3, 2]
# Output: 1
# Challenge: Find a way to do this using O(1) memory.


def single_number(nums):
    result = 0
    for element in nums:
        result ^= element
    return result


# 1
print(single_number([4, 3, 2, 4, 1, 3, 2]))
