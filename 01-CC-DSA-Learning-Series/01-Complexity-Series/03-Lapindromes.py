"""
problem statement - https://www.codechef.com/LRNDSA01/problems/LAPIN
"""

def char_to_ASCII(str_list):
    """
    converts a list of char into their ASCII counterparts
    
    inp: list of char
    returns: list of ASCII counterparts of char present in input list 
    """
    num_list = []
    for i in str_list:
        num_list.append(ord(i))
    return num_list


def lapindrome_test(string):
    """
    checks whether a given string is lapindrome or not.
    The logic used here is to convert the string into ASCII form and compare the sums of two halves

    inp: string
    returns: "Yes" or "No" depending upon result
    """
    string = string.lower()              # making string case all lower

    # spliting the string into two equal halves
    str_list = list(string)              # converting the string to list
    str_1 = str_list[:len(str_list)//2]
    str_2 = str_list[len(str_list)//2 if len(str_list)%2 == 0 else (len(str_list)//2) + 1:] # dropping the middle char if len is odd

    # convert char to ASCII
    num_list_1 = char_to_ASCII(str_1)
    num_list_2 = char_to_ASCII(str_2)

    # compare the above lists
    if sum(num_list_1) == sum(num_list_2):
        print("YES")
    else:
        print("NO")

# driver code
if __name__=="__main__":
    test_cases = int(input())
    for i in range(0, test_cases):
        test_case = input() 
        lapindrome_test(test_case)