class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # base case
        if numRows == 1:
            return s
        
        # create a list for each numRows
        res = [[] for i in range(0, numRows)]
        
        # delta manages which way i moves.
        # for example, the movement in numRows = 3 would be 1,2,3 and then 2, 1 and so on
        delta = -1
        i = 0
        for char in s:
            res[i].append(char)
            if i == 0 or i == numRows - 1:
                delta *= -1
            i += delta
        
        # combine elements of all the lists
        res_vec = []
        for i in res:
            res_vec.append("".join(i))
        
        return "".join(res_vec)