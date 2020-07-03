import math

def arrangeCoins(self, n: int) -> int:
    # start = 1
    # count = 0
    # while n>0:
    #     n = n - start
    #     if n < 0:
    #         return count
    #     else:
    #         count += 1
    #         start += 1
    # return count
    
    k = int(math.sqrt(2*n))
    sum_ = int(k*(k+1)/2)
    if sum_ > n:
        return k - 1
    else:
        return k