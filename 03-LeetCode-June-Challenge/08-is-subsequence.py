class Solution:
    def isSubsequence(self, s, t):
        if len(s) == len(t) and s == t:
            return True
        
        elif len(s) == len(t) and s != t:
            return False
        
        else:
            s, t = list(s), list(t)
            flag = 0
            for i in s:
                if i in t:
                    t = t[t.index(i) + 1:]
                    continue
                else:
                    flag = 1
                    return False
            if flag == 0:
                return True