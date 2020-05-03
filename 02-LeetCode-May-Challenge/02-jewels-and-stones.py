from collections import defaultdict

def list_to_dict(list_):
    """
    converts a list to dict
    """
    dict_ = defaultdict(int)
    for i in list_:
        dict_[i] += 1
    
    return dict_

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # convert J and S to lists
        J, S = list(J), list(S)
        
        # convert S to dict
        S = list_to_dict(S)
        
        sum = 0
        for j in J:
            sum += S.get(j, 0)
        
        return sum