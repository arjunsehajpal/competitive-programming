def decimal_to_binary(n, num_list):
    """
    converts the decimal number to binary number
    """
    # base case
    if n <= 1:
        num_list.append(n)
        num_list = list(reversed(num_list))
        return "".join([str(ele) for ele in num_list]), len(num_list)
    
    # recurssive case
    else:
        num_list.append(n%2)
        return decimal_to_binary(n//2, num_list)

def binary_to_decimal(b_num):
    """
    converts binary number to decimal
    """
    d_num, i = 0, 0
    while(b_num != 0):
        temp = b_num % 10
        d_num = d_num + temp * pow(2, i)
        b_num = b_num//10
        i += 1
    return d_num

def find_complement(num):
    """
    finds the complement of given num
    """
    # converting the number to binary
    b_num, l = decimal_to_binary(num, num_list = [])
    b_num = int(b_num)
    order = 2**l - 1
    order, l = decimal_to_binary(order, num_list = [])
    order = int(order)
    complement = order - b_num
    return binary_to_decimal(complement)


def find_complement_optimized(num):
    """
    uses binary operations to calculate the complement
    """
    # handling base case
    if num == 0:
        return 1

    temp = num    # create temp variable     
    order = 0     # calculate the order. If the number is 5 then order is 7, as biggest three digit binary number is 111 (i.e. 7)

    while temp > 0:
        temp = temp >> 1    # shifting right to calculate number of bit operations required to make it zero
        order = order << 1  # shifting the 0 left the same number of times, to calculate the order
        order += 1          # adding 1
    
    # returning the OR or order and num.
    return order ^ num



# driver code
if __name__=="__main__":
    print(find_complement_optimized(5))