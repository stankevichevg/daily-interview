# You are given a positive integer N which represents the number of steps in a staircase.
# You can either climb 1 or 2 steps at a time.
# Write a function that returns the number of unique ways to climb the stairs.
# Can you find a solution in O(n) time?


def staircase(n):
    if n < 3:
        return n
    first_back = 2
    second_back = 1
    current_step = 3
    while current_step < n:
        first_back_mem = first_back
        first_back = first_back + second_back
        second_back = first_back_mem
        current_step += 1
    return first_back + second_back


print(staircase(4))
# 5
print(staircase(5))
# 8
