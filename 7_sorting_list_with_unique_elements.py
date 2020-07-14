# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
# Challenge: Try sorting the list using constant space.
#
# Example 1:
# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]
def sortNums(nums):
    one_counter = 0
    two_counter = 0
    three_counter = 0
    for element in nums:
        if element == 1:
            one_counter += 1
        elif element == 2:
            two_counter += 1
        else:
            three_counter += 1
    result = []
    while one_counter != 0:
        result.append(1)
        one_counter -= 1
    while two_counter != 0:
        result.append(2)
        two_counter -= 1
    while three_counter != 0:
        result.append(3)
        three_counter -= 1
    return result


# [1, 1, 2, 2, 3, 3, 3]
print(sortNums([3, 3, 2, 1, 3, 2, 1]))
