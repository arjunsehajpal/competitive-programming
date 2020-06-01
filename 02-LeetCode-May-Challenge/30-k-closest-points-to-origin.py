def k_closest_to_origin(points_list, k):
    """
    args: points_list (list of lists)
          k (number of closest points to be calculated)
    returns: a list of lists
    """
    points.sort(key = lambda x: x[0]**2 + x[1]**2)
    return points[:k]



# driver code
if __name__=="__main__":
    # test case 01
    points = [[1,3],[-2,2]]
    K = 1
    ans = k_closest_to_origin(points_list = points, k = K)
    print(ans)

    # test case 02
    points = [[3,3],[5,-1],[-2,4]]
    K = 2
    ans = k_closest_to_origin(points_list = points, k = K)
    print(ans)