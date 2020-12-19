class Solution:
    def longestPalindrome(self, s: str) -> str:
        # base case
        if self.checkPalindrome(s):
            return s
        
        max_len = 1
        max_str = s[0]
        
        for i in range(0, len(s) - 1):
            for j in range(0, len(s) - i):
                temp_str = s[j:j+i+1]
                if self.checkPalindrome(temp_str):
                    temp_len = len(temp_str)
                
                if temp_len > max_len:
                    max_len = temp_len
                    max_str = temp_str
        
        return max_str
        
    def checkPalindrome(self, str_):
        """
        check if a given string is palindrome or not
        """
        rev_str = str_[::-1]
        if str_ == rev_str:
            return True
        else:
            return False