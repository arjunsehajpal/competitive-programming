from collections import defaultdict

def create_freq_dict(list_):
    """
    creates a dictionary with key being list element and
    its value being the frequency of the element 
    """
    dict_ = defaultdict(int)
    for i in list_:
        dict_[i] += 1
    return dict_

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # convert the list to frequency dictionary
        freq_dict = create_freq_dict(nums)
        return max(freq_dict, key = freq_dict.get)
        
        # # optimizing memory
        # nums.sort()
        # length = len(nums)
        # return nums[length//2]