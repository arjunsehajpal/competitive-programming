def max_uncrossed_lines(A, B):
    """
    a function to determines the max number of uncrossed lines from A to B

    args: A (array of integers)
          B (array of integers)
    returns: int (number of uncrossed lines)
    """
    # padding A and B to handle edge cases
    A = [0] + A
    B = [0] + B

    # initialize a matrix of zeros with rows representing A
    # and columns representing B
    n = len(A)
    m = len(B)

    matrix = [([0] * m) for r in range(n)]

    # in the loop below, r and c are used to access the elements of matrix
    # the same indices are used to access the elements of A and B
    # Here, each element of represent A upto that element
    # similary, for B

    for r in range(1, n):
        for c in range(1, m):
            if A[r] == B[c]:
                # new uncrossed line, add 1 to current max value
                matrix[r][c] = matrix[r - 1][c - 1] + 1
            else:
                # no new line, inherit the current max value
                matrix[r][c] = max(matrix[r][c - 1], matrix[r - 1][c])
    return matrix[-1][-1]