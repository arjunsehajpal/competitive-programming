class Solution:
    def reverse(self, x: int) -> int:
        # base case
        if x > 2**31-1 or x < -2**31:
            return 0
        
        if x > 0:
            x = str(x)
            rev_x = int(x[::-1]) # reversing the string
        else:
            x = str(abs(x))
            rev_x = -1*(int(x[::-1]))
        
        if rev_x > 2**31-1 or rev_x < -2**31:
            return 0
        else:
            return rev_x