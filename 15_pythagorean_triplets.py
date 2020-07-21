# Given a list of numbers, find if there exists a pythagorean triplet in that list.
# A pythagorean triplet is 3 variables a, b, c where a2 + b2 = c2

# Example:
# Input: [3, 5, 12, 5, 13]
# Output: True
# Here, 52 + 122 = 132.


def find_pythagorean_triplets(nums):
    if len(nums) < 3:
        return False
    sorted_nums = sorted(nums)
    sorted_squared_nums = [e * e for e in sorted_nums]
    for pos in range(2, len(nums)):
        if is_pair_with_sum(sorted_squared_nums, 0, pos, sorted_squared_nums[pos]):
            return True
    return False


def is_pair_with_sum(nums, start, end, sum):
    left = start
    right = end - 1
    while left < right:
        if nums[left] + nums[right] == sum:
            return True
        elif nums[left] + nums[right] < sum:
            left += 1
        else:
            right += 1
    return False


# True
print(find_pythagorean_triplets([3, 12, 5, 13]))
