def check_inclusion(s1, s2):
    # base case:
    if len(s1) > len(s2):
        return False
    
    # create an array of len 26, representing every alphabet
    pchar = [0]*26

    # update the frequency list for each character in pchar based on s1
    for char in s1:
        pchar[ord(char) - ord("a")] += 1
    
    # first pass of pchar over s2
    start = 0
    for i in range(0, len(s1)):
        pchar[ord(s2[i]) - ord("a")] -= 1

    # creating a mismatch count
    # if only mismatch count == 0, then s2 contains permutation of s1
    mismatch_count = 0
    for j in pchar:
        if j != 0:
            mismatch_count += 1
    
    # if 0, s2 contains permutation of s1
    if mismatch_count == 0:
        return True
    # update start as our first is complete
    start += 1

    # looping through the remaining string
    while start <= (len(s2) - len(s1)):
        # as we pass over s2 with stride of 1,
        # i1 represents the string element removed from the window
        # and i2 represents the string element added to the window
        i1 = ord(s2[start - 1]) - ord("a")
        i2 = ord(s2[start + len(s1) - 1]) - ord("a")

        # updating pchar accordingly.
        # As i1 is removed from the window, increment it's freq count
        pchar[i1] += 1
        if pchar[i1] == 1:
            mismatch_count += 1
        elif pchar[i1] == 0:
            mismatch_count -= 1

        # As i2 is added to the window, decrement it's freq count
        pchar[i2] -= 1
        if pchar[i2] == -1:
            mismatch_count += 1
        elif pchar[i2] == 0:
            mismatch_count -= 1

        if mismatch_count == 0:
            return True 
        start += 1

    return False

def check_inclusion_hash(s1, s2):
    s1Len, s2Len = len(s1), len(s2)
    s1Hash, s2Hash = 0, 0
    if s1Len > s2Len:
        return False
    
    for i in range(s1Len):
        s1Hash, s2Hash = s1Hash + hash(s1[i]), s2Hash + hash(s2[i])
    if s1Hash == s2Hash:
        return True
    for i in range(s1Len, s2Len):
        s2Hash += hash(s2[i]) - hash(s2[i-s1Len])
        if s2Hash == s1Hash:
            return True
    return False


# driver code
if __name__=="__main__":
    # test case 01
    s1 = "ab" 
    s2 = "eidbaooo"
    ans = check_inclusion(s1 = s1, s2 = s2)
    print(ans)

    s1= "ab" 
    s2 = "eidboaoo"
    ans = check_inclusion(s1 = s1, s2 = s2)
    print(ans)