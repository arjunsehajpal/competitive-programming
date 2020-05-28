def bit_counter(num):
    """
    counts the number of 1s in each number till num

    args: num (int)
    returns: list
    """
    num_list = list(range(num + 1))
    resultant_list = []
    for i in range(0, len(num_list)):
        if num_list[i] == 0:
            resultant_list.append(0)
        elif num_list[i]%2 == 0:
            # print("{} ... {}".format(i, resultant_list))
            resultant_list.append(resultant_list[int(i/2)])
        else:
            # print("{} ... {}".format(i, resultant_list))
            # print(resultant_list[int(i/2)] + 1)
            resultant_list.append(resultant_list[int(i/2)] + 1)
    return resultant_list


# driver code
if __name__=="__main__":
    # test case 01
    num = 2
    ans = bit_counter(num)
    print(ans)

    num = 5
    ans = bit_counter(num)
    print(ans)