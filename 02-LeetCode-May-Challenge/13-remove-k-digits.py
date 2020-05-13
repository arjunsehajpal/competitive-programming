# import math

# def remove_str_char(str_, n):
#     """
#     removes the ith character from the string
#     """
#     new_str = ""
#     for i in range(0, len(str_)):
#         if i != n:
#             new_str = new_str + str_[i]
    
#     return new_str


# def remove_k_digits(num, k):
#     if len(num) == k:
#         return "0"
    
#     if k == 0:
#         return num
    
#     iter_len = len(num)

#     min_comb = math.inf
#     while k>0:
#         for i in range(0, iter_len):
#             new_str = remove_str_char(num, n = i)
#             int_str = int(new_str)
#             if int_str < min_comb:
#                 min_comb = int_str
#         num = str(min_comb)
#         k -= 1
#     return str(min_comb)

# def remove_k_digits(num, k, res = ""):
#     if len(num) == k:
#         return "0"
#     if k == 0:
#         return num
#     if len(num) <= k:
#         return

#     # find the smallest character among first k+1 character
#     min_index = 0
#     for i in range(1, k + 1):
#         if int(num[i]) < int(num[min_index]):
#             min_index = i
    
#     # append the smallest charater to result
#     res = res + num[min_index]

#     # decrement the k
#     k = k - 1
    
#     # create a new
#     num = num[min_index + 1: len(num)]
#     # print(num)
#     min_comb = math.inf
#     # print(k)
#     while k>0:
#         for i in range(0, len(num)):
#             new_str = remove_str_char(num, n = i)
#             int_str = int(new_str)
#             if int_str < min_comb:
#                 min_comb = int_str
#                 # print(min_comb)
#         num = str(min_comb)
#         k -= 1

#     return int(res + num)


def remove_k_digits(num, k):
    if len(num) == k:
        return "0"

    i = 0
    while k > 0:
        i = (i > 0) and (i - 1) or 0
        while(i < len(num) - 1 and num[i] <= num[i+1]):
            i += 1
        num = num[0:i] + num[i+1:]
        k -= 1 
    
    if len(num) == 0:
        return "0"
    
    return str(int(num))

def remove_k_digits_fastest(num, k):
    stack=[]
    print("Stack = ", stack)
    for n in num:
        print("n=", n)
        while k and stack and stack[-1]>n:
            print(">>>", stack[-1])
            print("Stack inside while = ", stack)
            stack.pop()
            print("Stack after pop = ", stack)
            k-=1
        stack.append(n)
        print("Stack append = ", stack)
    
    stack = stack[:-k] if k else stack
    print(stack)
    return "".join(stack).lstrip('0') or "0"


# driver code
if __name__=="__main__":
    # test case 01
    num_1 = "1432219" 
    k_1 = 3
    ans_1 = remove_k_digits(num = num_1, k = k_1)
    print(ans_1)

    # # test case 02
    # num_2 = "10200" 
    # k_2 = 1
    # ans_2 = remove_k_digits(num = num_2, k = k_2)
    # print(ans_2)
    
    # # test case 03
    # num_3 = "10" 
    # k_3 = 2
    # ans_3 = remove_k_digits(num = num_3, k = k_3)
    # print(ans_3)

    # # test case 04 -> 11
    # num_4 = "112"
    # k_4 = 1
    # ans_4 = remove_k_digits(num = num_4, k = k_4)
    # print(ans_4)