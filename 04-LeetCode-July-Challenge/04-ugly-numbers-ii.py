class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # storing ugly numbers
        ugly_num_list = [0] * n
        
        # add 1 as first ugly number 
        ugly_num_list[0] = 1
        
        # i2, i3 and i5 will indicate indices for 2, 3 and 5
        i2 = i3 = i5 = 0
        
        # set initial multiples
        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5
        
        for j in range(1, n):
            ugly_num_list[j] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            
            if ugly_num_list[j] == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly_num_list[i2]*2
                
            if ugly_num_list[j] == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly_num_list[i3]*3
                
            if ugly_num_list[j] == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly_num_list[i5]*5
                
        return ugly_num_list[-1]