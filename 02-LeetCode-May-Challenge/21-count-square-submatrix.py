import numpy as np

def count_squares(mat):
    """
    counts the number of perfect squares in the matrix

    args: mat (matrix)
    returns: int (number matrix)
    """
    if mat is None or len(mat) == 0:
        return 0

    row = len(mat)
    col = len(mat[0])

    count = [0]*col

    tl = 0
    result = 0
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 1:
                t = 0 if i == 0 else count[j]
                l = 0 if i == 0 else count[j - 1]
                count[j] = 1 + min(min(t, l), tl)
                result += count[j]

                tl = 0 if j == col-1 else t
            else:
                count[j] = 0
    return result



# driver code
if __name__=="__main__":
    # test case 01
    matrix = [
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [0, 1, 1, 1]
            ]
    ans = count_squares(matrix)
    print(ans)
