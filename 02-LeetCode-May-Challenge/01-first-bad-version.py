# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower = 1
        upper = n
        while lower < upper:
            mid_value = int(lower + (upper - lower)/2)
            
            if isBadVersion(mid_value):
                upper = mid_value
            else:
                lower = mid_value + 1
        
        return lower