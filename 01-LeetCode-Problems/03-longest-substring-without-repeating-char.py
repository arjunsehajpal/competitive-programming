class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_ = {}
        max_len = 0
        
        # set the initial point of the window to 0
        start = 0
        for i in range(0, len(s)):
            if s[i] in dict_:
                start = max(start, dict_[s[i]] + 1)
                
            # updating the last seen value of the character
            dict_[s[i]] = i
            max_len = max(max_len, i - start + 1)
        
        return max_len