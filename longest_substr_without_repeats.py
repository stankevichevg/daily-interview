# Given a string, find the length of the longest substring without repeating characters.
# Can you find a solution in linear time?


class Solution:

    def length_of_longest_substring(self, s):
        max_length = 0
        tail_set = set()
        tail_set_start = 0
        tail_set_end = 0
        for i, char in enumerate(s):
            if char not in tail_set:
                tail_set.add(char)
                if max_length < len(tail_set):
                    max_length = len(tail_set)
            else:
                for j in range(tail_set_start, tail_set_end + 1):
                    tail_set.remove(s[j])
                    if s[j] == char:
                        break
                tail_set.add(char)
                tail_set_start = j + 1
            tail_set_end = i;
        return max_length


print(Solution().length_of_longest_substring('abrkaabcdefghijjxxx'))
