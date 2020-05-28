class Solution:
    def findMaxLength(self, nums):
        dict_map = {0: -1}
        running_sum = 0
        max_len = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                running_sum -= 1
            else:
                running_sum += 1
            if running_sum not in dict_map:
                dict_map[running_sum] = i
                # print(dict_map)
            else:
                # print("rs = ", running_sum)
                max_len = max(max_len, i - dict_map[running_sum])
                # print("ml = ", max_len)
        return max_len