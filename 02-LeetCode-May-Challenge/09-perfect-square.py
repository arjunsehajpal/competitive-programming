def is_perfect_square(num):
    """
    returns True if number is perfect square, else return false
    """
    # base case
    if num < 2:
        return True

    left, right = 2, num // 2
    
    while left <= right:
        mid = (left + right) // 2
        print("left = ", left)
        print("right = ", right)
        print("mid = ", mid)
        guess_sqr = mid * mid
        if guess_sqr == num:
            return True
        elif guess_sqr > num:
            right = mid - 1
        else:
            left = mid + 1
    
    return False

print(is_perfect_square(13))