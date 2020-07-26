# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# Example:
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
#
# Here is the method signature:


def min_sub_array_len(nums, s):
    k = len(nums)
    tail_sum = nums[0]
    ts = 0
    for size in range(2, len(nums) + 1):
        element = nums[size-1]
        if element >= s:
            return 1
        else:
            tail_sum += element
            while tail_sum - nums[ts] >= s:
                tail_sum -= nums[ts]
                ts += 1
            if tail_sum >= s and k > size - ts:
                k = size - ts
    return k


print(min_sub_array_len([2, 3, 1, 2, 4, 3], 7))
# 2

# [...] - some array of length N
# k - current length of optimal array for current array
# tail - smallest possible elements subarray at the end of array that sum up to s or bigger
# tail_sum - sum of the tail
# ts - start of the tail
# if we add a new element:
#   1. if element => s then return 1
#   2. else
#       if element + tail_sum > s then move ts right while element + tail_sum > s
#       if element + tail_sum > s AND len(tail) < k then k = len(tail)
