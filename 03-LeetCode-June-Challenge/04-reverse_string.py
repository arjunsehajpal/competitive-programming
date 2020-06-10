def reverse_words(s_list, i):
    if i == len(s_list)//2:
        return " ".join(s_list)
    
    else:
        s_list[i], s_list[len(s_list) - i - 1] = s_list[len(s_list) - i - 1], s_list[i]
        return reverse_words(s_list, i = i + 1)


def reverse_str_word_wise(str_):
    """
    reverses the string word by word
    """
    s_list = str_.split(" ")
    ans = reverse_words(s_list, i = 0)
    return ans


# driver code
if __name__=="__main__":
    str_ = "I Love Sports"
    ans = reverse_str_word_wise(str_)
    print(ans)