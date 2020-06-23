from math import comb # works with py3.8 or above

class Solution:
    def getRow(self, rowIndex):
        arr = []
        for i in range(0, rowIndex + 1):
            arr.append(comb(rowIndex, i))
        return arr