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

def canConstruct(ransomNote, magazine):
    """
    returns whether we can create ransom note (str 1) from the newspaper cuttings (str2)
    """
    # convert both strings to lists
    ransomNote, magazine = list(ransomNote), list(magazine)

    # create a frequency dictionary for str2
    magazine_dict = create_freq_dict(magazine)
    print(magazine_dict)

    for i in ransomNote:
        if i in magazine_dict and magazine_dict[i] > 0:
            magazine_dict[i] -= 1
            continue
        else:
            return False
    return True




print(canConstruct("a", "b"))
print(canConstruct("aa", "ab"))
print(canConstruct("aa", "aab"))