# Given two strings, determine the edit distance between them.
# The edit distance is defined as the minimum number of edits
# (insertion, deletion, or substitution) needed to change one string to the other.

# For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).

# Here's the signature:


def distance(s1, s2, fl=None, sl=None):
    fl = fl if fl is not None else len(s1)
    sl = sl if sl is not None else len(s2)
    if fl == 0:
        return sl
    if sl == 0:
        return fl
    if s1[fl-1] == s2[sl-1]:
        return distance(s1, s2, fl-1, sl-1)
    return 1 + min(
        distance(s1, s2, fl, sl-1),
        distance(s1, s2, fl-1, sl),
        distance(s1, s2, fl-1, sl-1)
    )


print(distance('biting', 'sitting'))
# 2
