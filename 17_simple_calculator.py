# Given a mathematical expression with just single digits, plus signs,
# negative signs, and brackets, evaluate the expression.
# Assume the expression is properly formed.

# Example:
# Input: - ( 3 + ( 2 - 1 ) )
# Output: -4
# Here's the function signature:


def eval(expression):
    def eval_expression(expr_arr, start):
        acc = 0
        cur_sign = 1
        pos = start
        while pos != len(expr_arr) and expr_arr[pos] != ")":
            if expr_arr[pos] == "-":
                cur_sign = -1
            elif expr_arr[pos] == "+":
                cur_sign = 1
            elif expr_arr[pos] == "(":
                expr_value, jump = eval_expression(expr_arr, pos + 1)
                acc += cur_sign * expr_value
                pos = jump
            else:
                acc += cur_sign * int(expr_arr[pos])
            pos += 1
        return acc, pos
    return eval_expression(expression.split(" "), 0)[0]


print(eval('- ( 3 + ( 2 - 1 ) )'))
# -4
