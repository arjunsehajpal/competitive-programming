import string

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(0, len(s)):
            if s[0] not in s[1:]:
                return i
            else:
                s = s[1:] + s[0]
                continue
        return -1

###########################
##### Fastest Solution ####
###########################

def first_unique_char(s):
    len_str = len(s)    # get len of the string
    for c in string.ascii_lowercase:
        left = s.find(c)
        if left != -1 and left == s.rfind(c):
            len_str = min(left, len_str)
    return len_str if len_str != len(s) else -1


# driver code
if __name__=="__main__":
    # test case 01
    uniq_char = first_unique_char("loveleetcode")
    print("First Test Case = {}".format(uniq_char))

    # test case 02
    uniq_char = first_unique_char("cc")
    print("Second Test Case = {}".format(uniq_char))

    
