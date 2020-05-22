from collections import defaultdict
import operator

def list_to_dict(list_):
    dict_ = defaultdict(int)
    for i in list_:
        dict_[i] += 1 
    
    dict_ = dict(sorted(dict_.items(), key = operator.itemgetter(1), reverse = True))
    return dict_

class Solution:
    def frequencySort(self, s: str) -> str:
        s = list(s)
        s_dict = list_to_dict(s)
        result = []
        for i, j in s_dict.items():
            result.append(i*j)
        
        return "".join(result)