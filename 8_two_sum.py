# You are given a list of numbers, and a target number k.
# Return whether or not there are two numbers in the list that add up to k.
#
# Example:
# Given [4, 7, 1 , -3, 2] and k = 5,
# return true since 4 + 1 = 5.
# Try to do it in a single pass of the list.


def two_sum(list, k):
    rests = set()
    for element in list:
        if element in rests:
            return True
        rests.add(k - element)
    return False


print(two_sum([4, 7, 1, -3, 2], 5))
# True
