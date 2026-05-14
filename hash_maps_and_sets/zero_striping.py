"""
https://bytebytego.com/exercises/coding-patterns/hash-maps-and-sets/zero-striping

For each zero in an m x n matrix, set its entire row and column to zero in place.
"""


# Time complexity: O(m * n) same as below
# Space complexity: O(1) since the first row and first column are used as markers to track which rows and columns
# contain zeros instead of using auxiliary data structures
def zero_striping(matrix: list[list[int]]):
    if not matrix or not matrix[0]:
        return None

    # Remember whether the first row or first column already contains a 0.
    # We need this information because these cells are later re-used as markers.
    first_row_has_zero = 0 in matrix[0]
    first_column_has_zero = False

    for r in range(len(matrix)):
        if matrix[r][0] == 0:
            first_column_has_zero = True
            break

    # Use the first row and first column as marker storage.
    # When a 0 is found at matrix[i][j], we place markers at:
    # matrix[i][0]  -> row i should be zeroed
    # matrix[0][j]  -> column j should be zeroed
    #
    # Example:
    #
    # Original matrix
    #
    #      0   1   2   3   4
    #    +---+---+---+---+---+
    #  0 | 1 | 2 | 3 | 4 | 5 |
    #    +---+---+---+---+---+
    #  1 | 6 | 0 | 6 | 9 |10 |
    #    +---+---+---+---+---+
    #  2 |11 |12 |13 |14 |15 |
    #    +---+---+---+---+---+
    #  3 |16 |17 |18 |19 | 0 |
    #    +---+---+---+---+---+
    #
    # After marking (X denotes a marker):
    #
    #      0   1   2   3   4
    #    +---+---+---+---+---+
    #  0 | 1 | X | 3 | 4 | X |
    #    +---+---+---+---+---+
    #  1 | X | 0 | 6 | 9 |10 |
    #    +---+---+---+---+---+
    #  2 |11 |12 |13 |14 |15 |
    #    +---+---+---+---+---+
    #  3 | X |17 |18 |19 | 0 |
    #    +---+---+---+---+---+
    #
    # Use the first row and column as markers. If an element in the submatrix
    # is 0, mark its corresponding row and column in the first row and first
    # column as 0.
    for r in range(1, len(matrix)):
        for c in range(1, len(matrix[0])):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0

    # Update the submatrix using the markers in the first row and first column.
    # If either marker is 0, the current cell belongs to a row or column that
    # must be zeroed.
    for r in range(1, len(matrix)):
        for c in range(1, len(matrix[0])):
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0

    # If the first row originally contained a 0, zero the entire row.
    if first_row_has_zero:
        for c in range(len(matrix[0])):
            matrix[0][c] = 0

    # If the first column originally contained a 0, zero the entire column.
    if first_column_has_zero:
        for r in range(len(matrix)):
            matrix[r][0] = 0

    return None


# Alternative code
# This solution uses slightly less memory with the same time complexity
# The micro-optimization lies in using 1 list[tuple[int, int]] vs. 2 sets as shown below
# def zero_striping(matrix: list[list[int]]):
#     if not matrix or not matrix[0]:
#         return None
#
#     coordinates: list[tuple[int, int]] = []
#     for x in range(len(matrix)):
#         for y in range(len(matrix[x])):
#             if matrix[x][y] == 0:
#                 coordinates.append((x, y))
#
#     for coord in coordinates:
#         x, y = coord
#         for row in range(len(matrix)):
#             matrix[row][y] = 0
#
#         for col in range(len(matrix[x])):
#             matrix[x][col] = 0
#
#     return None


# Alternative code - Book's solution
# Time complexity: O(m * n)
# Space complexity: O(m + n) since it uses 2 sets
# def zero_striping(matrix: list[list[int]]):
#     if not matrix or not matrix[0]:
#             return None
#
#         m = len(matrix)
#         n = len(matrix[0])
#         zero_rows = set()
#         zero_cols = set()
#
#         for r in range(m):
#             for c in range(n):
#                 if matrix[r][c] == 0:
#                     zero_rows.add(r)
#                     zero_cols.add(c)
#
#         # The set in membership checks within the if statement are each O(1) on average
#         for r in range(m):
#             for c in range(n):
#                 if r in zero_rows or c in zero_cols:
#                     matrix[r][c] = 0
#
#         return None


if __name__ == "__main__":
    m = [
        [1, 2, 3, 4, 5],
        [6, 0, 6, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 0],
    ]
    zero_striping(m)
    assert m == [
        [1, 0, 3, 4, 0],
        [0, 0, 0, 0, 0],
        [11, 0, 13, 14, 0],
        [0, 0, 0, 0, 0],
    ]
