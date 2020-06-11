class Solution:
    def searchInsert(self, nums, target) -> int:
        idx, last_idx = 0, len(nums) - 1
        
        while idx <= last_idx:
            # binary search
            mid_idx = idx + (last_idx - idx)//2
            
            if nums[mid_idx] == target:
                return mid_idx
            
            if nums[mid_idx] < target:
                idx = mid_idx + 1
            else:
                last_idx = mid_idx - 1
            
        return idx