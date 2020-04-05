def reverse_number_fn(num, rev_num):
    """
    reverses the number
    """
    # base case
    if num//10 < 1:
        return rev_num * 10 + num
    
    else:
        quotient = num//10
        remainder = num%10
        rev_num = rev_num*10 + remainder
        return reverse_number_fn(quotient, rev_num)



# driver code
if __name__=="__main__":
    test_cases = int(input())

    input_list = []
    for i in range(0, test_cases):
        inp = int(input())
        input_list.append(inp)

    for i in input_list:
        print(reverse_number_fn(num = i, rev_num = 0))

