def single_nonduplicate_element(list_):
    """
    returns the single non-duplicate element from the list
    """
    element = sum(set(list_))*2 - sum(list_)
    return element


# driver code
if __name__=="__main__":
    # test case 01
    list_1 = [1, 2, 2, 3, 3, 4, 4]
    ans_1 = single_nonduplicate_element(list_1)
    print(ans_1)

    # test case 02
    list_2 = [3,3,7,7,10,11,11]
    ans_2 = single_nonduplicate_element(list_2)
    print(ans_2)