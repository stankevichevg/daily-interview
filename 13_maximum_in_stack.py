# Implement a class for a stack that supports all the regular functions (push, pop) and
# an additional function of max() which returns the maximum element in the stack (return None if the stack is empty).
# Each method should run in constant time.


class MaxStack:
    def __init__(self):
        self.stack = []
        self.current_max = None

    def push(self, val):
        prev_max = self.current_max
        self.current_max = val if self.current_max is None else max(self.current_max, val)
        self.stack.append((val, prev_max))

    def pop(self):
        if len(self.stack) == 0:
            return None
        val, prev_max = self.stack.pop()
        self.current_max = prev_max
        return val

    def max(self):
        return self.current_max


s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2