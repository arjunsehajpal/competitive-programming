class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        checking if a number is palindrome
        without converting it to string
        """
        # base case
        if x < 0:
            return False
        if x < 10 and x >= 0:
            return True
        
        comp = x
        rev_num = 0
        rem = 0
        while x // 10 != 0:
            rem = x%10
            x = x//10
            rev_num = (rev_num + rem) * 10
        
        rev_num = rev_num + x
        if rev_num == comp:
            return True
        else:
            return False