# You are given a 2D array of characters, and a target string.
# Return whether or not the word target word exists in the matrix.
# Unlike a standard word search, the word must be either going left-to-right, or top-to-bottom in the matrix.

# Example:
#
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
#
# Given this matrix, and the target word FOAM, you should return true,
# as it can be found going up-to-down in the first column.

# Here's the function signature:


def vertical_search(matrix, word, row, col):
    if row > len(matrix) - len(word):
        return False
    else:
        for i in range(0, len(word)):
            if word[i] != matrix[row+i][col]:
                return False
        return True


def horizontal_search(matrix, word, row, col):
    if col > len(matrix[row]) - len(word):
        return False
    else:
        for i in range(0, len(word)):
            if word[i] != matrix[row][col+i]:
                return False
        return True


def word_search(matrix, word):
    for row in range(0, len(matrix)):
        for col in range(0, len(matrix[row])):
            if word[0] == matrix[row][col]:
                if horizontal_search(matrix, word, row, col):
                    return True
                if vertical_search(matrix, word, row, col):
                    return True
    return False


# Fill this in.
matrix = [
    ['F', 'O', 'A', 'M'],
    ['O', 'B', 'Q', 'P'],
    ['A', 'N', 'O', 'B'],
    ['N', 'A', 'S', 'S']]

# True
print(word_search(matrix, 'FOAM'))
