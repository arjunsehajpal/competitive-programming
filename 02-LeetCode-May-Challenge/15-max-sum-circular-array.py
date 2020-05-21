import math

def max_sub_array_sum_circular(A):
    total_sum = 0
    max_ending_at = 0
    min_ending_at = 0
    max_sum = -math.inf
    min_sum = math.inf
    
    for x in A:
        total_sum += x
        max_ending_at = max(max_ending_at + x, x)
        max_sum = max(max_ending_at, max_sum)
        min_ending_at = min(min_ending_at + x, x)
        min_sum = min(min_ending_at, min_sum)
    
    if max_sum > 0:
        return max(max_sum, total_sum - min_sum)
    return max_sum

# driver code
if __name__=="__main__":
    arr = [1,-2,3,-2]
    ans = max_sub_array_sum_circular(arr)
    print(ans)