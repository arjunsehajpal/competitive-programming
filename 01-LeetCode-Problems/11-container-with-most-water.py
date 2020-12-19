class Solution:
    def maxArea(self, height) -> int:
        # Brute Force Solution - Time Error #
        # max_area = 0
        # curr_area = 0
        # for i in range(0, len(height) - 1):
        #     for j in range(1, len(height)):
        #         h = height[i] if height[i] < height[j] else height[j]
        #         l = j - i
        #         curr_area = h * l
        #         if curr_area > max_area:
        #             max_area = curr_area
        #         else:
        #             curr_area = 0
        # return max_area
        
        
        # Accepted Solution
        max_area = 0
        curr_area = 0
        i = 0                # start index
        j = len(height) - 1  # end index
        while i < j:
            # measure the area
            h = height[i] if height[i] < height[j] else height[j]
            l = j - i
            curr_area = h * l
            if curr_area > max_area:
                max_area = curr_area
            
            # increment or decrement whichever index has the smaller height
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
        