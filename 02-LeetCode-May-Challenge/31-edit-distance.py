def distance_recur(word1, word2, l1, l2):
    """
    measures the number of iteration required to change one str to another
    """
    # creating a matrix to store the results of the sub-problems
    l1 = len(word1)
    l2 = len(word2)

    dp = [[0 for x in range(l2+1)] for y in range(l1 + 1)]
    for i in range(0, l1 + 1):
        for j in range(0, l2 + 1):
            # if word1 is empty, only option is to add all the chars of word2
            if i == 0:
                dp[i][j] = j
            
            # else if, word2 is empty, we need to remove all the chars of word1
            elif j == 0:
                dp[i][j] = i
            
            # if last character is same then recur without the last character
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            # if last chars are different, consider all possible solutions
            else:
                dp[i][j] = 1 + min(
                    dp[i][j-1],
                    dp[i-1][j],
                    dp[i-1][j-1]
                )

    return dp[l1][l2]




def edit_distance(word1, word2):
    """
    wrapper function of distance_recur function 
    """
    l1 = len(word1)
    l2 = len(word2)
    dist = distance_recur(word1, word2, l1, l2)
    return dist


# driver code
if __name__=="__main__":
    # test case 01
    word1 = "horse"
    word2 = "ros"
    ans = edit_distance(word1, word2)
    print(ans)

    # test case 02
    word1 = "intention"
    word2 = "execution"
    ans = edit_distance(word1, word2)
    print(ans) 