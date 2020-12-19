class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        #         else:
        #             continue
        
        #####################
        #### Approach 02 ####
        #####################
        
        dict_ = {}
        for i in range(0, len(nums)):
            # create a dictionary with key being target - value and value being index
            dict_[target - nums[i]] = i
            
        for i in range(0, len(nums)):
            ans = dict_.get(nums[i], -1)
            if ans != -1 and ans != i:
                return [i, ans]
            else:
                continue