def is_anagram(str1, str2):
    """
    checks if str1 and str2 are anagram of each other or not
    """
    # base case
    if len(str1) != len(str2):
        return False 

    count1 = 0
    count2 = 0
    for i in range(0, len(str1)):
        count1 += ord(str1[i]) - ord("a")
        count2 += ord(str2[i]) - ord("a")
    
    if count1 == count2:
        if sorted(str1) == sorted(str2):
            return True
    
    return False


def anagram_count(s, p):
    """
    received time limit exceeded error
    """
    n = len(p)
    index_list = []
    for i in range(n, len(s) + 1):
        sub_s = s[i - n: i]
        if is_anagram(sub_s, p):
            index_list.append(i - n)
        
    return index_list


def anagram_count_2(s, p):
    """
    Time - O(n)
    """
    result = []
    if len(p) > len(s):
        return result
    
    pchar = [0]*26
    for char in p:
        pchar[ord(char) - ord("a")] += 1
    
    start = 0
    for i in range(0, len(p)):
        pchar[ord(s[i]) - ord("a")] -= 1
    
    mismatch_count = 0
    for j in pchar:
        if j != 0:
            mismatch_count += 1
            
    if mismatch_count == 0:
        result.append(start)
    start += 1
    
    while start <= (len(s) - len(p)):
        i1 = ord(s[start - 1]) - ord("a")
        i2 = ord(s[start + len(p) - 1]) - ord("a")
        pchar[i1] += 1
        if pchar[i1] == 1:
            mismatch_count += 1
        elif pchar[i1] == 0:
            mismatch_count -= 1
            
        pchar[i2] -= 1
        if pchar[i2] == -1:
            mismatch_count += 1
        elif pchar[i2] == 0:
            mismatch_count -= 1
            
        if mismatch_count == 0:
            result.append(start)
        start += 1 
    
    return result


# driver code
if __name__=="__main__":
    # test case 01
    sup_str = "cbaebabacd" 
    sub_str = "abc"
    ans = anagram_count_2(s = sup_str, p = sub_str)
    print(ans)

    # test case 02
    sup_str = "abab" 
    sub_str = "ab"
    ans = anagram_count_2(s = sup_str, p = sub_str)
    print(ans)

    # test case 03
    sup_str = "af"
    sub_str = "be"
    ans = anagram_count_2(s = sup_str, p = sub_str)
    print(ans)