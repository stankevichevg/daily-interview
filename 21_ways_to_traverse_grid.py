# You 2 integers n and m representing an n by m grid, determine the number of ways you can get from
# the top-left to the bottom-right of the matrix y going only right or down.
#
# Example:
# n = 2, m = 2
#
# This should return 2, since the only possible routes are:
# Right, down
# Down, right.
#
# Here's the signature:


def num_ways(n, m):
    matrix = [[0] * m for i in range(n)]
    matrix[0][0] = 1
    for i in range(1, min(m, n)):
        matrix[0][i] = 1
        matrix[i][0] = 1
        for row in range(1, i):
            matrix[row][i] = matrix[row][i-1] + matrix[row-1][i]
        for col in range(1, i + 1):
            matrix[i][col] = matrix[i - 1][col] + matrix[i][col - 1]
    return matrix[n-1][m-1]


# 6
print(num_ways(3, 3))
