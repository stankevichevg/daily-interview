# Imagine you are building a compiler.
# Before running any code, the compiler must check that the parentheses in the program are balanced.
# Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.
#
# Example:
# Input: "((()))"
# Output: True
#
# Input: "[()]{}"
# Output: True
#
# Input: "({[)]"
# Output: False

class Solution:

    def is_valid(self, s):
        stack = []
        open_brackets = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif char == ')' or char == '}' or char == ']':
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if char not in open_brackets.keys() or top != open_brackets[char]:
                    return False
        return len(stack) == 0


s = "()(){(())"

# should return False
print(Solution().is_valid(s))

s = ""
# should return True
print(Solution().is_valid(s))

s = "([{}])()"
# should return True
print(Solution().is_valid(s))