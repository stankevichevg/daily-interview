# This problem was recently asked by Twitter:
# A palindrome is a sequence of characters that reads the same backwards and forwards.
# Given a string, s, find the longest palindromic substring in s.

# Example:
# Input: "banana"
# Output: "anana"
#
# Input: "million"
# Output: "illi"


class Solution:

    def longest_palindrome(self, s: str):
        start = 0
        end = 0
        for i in range(0, len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i + 1)
            mlen = max(len1, len2)
            if mlen > end - start + 1:
                start = i - int((mlen - 1) / 2)
                end = i + int(mlen / 2)
        return s[start: end + 1]

    def expand(self, s: str, left, right):
        if left > right or s is None:
            return 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


s = "racecar"
print(str(Solution().longest_palindrome(s)))
