class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_arr = self.merge(nums1, nums2)
        
        # median
        n = len(merged_arr)    # len of the array for median logic
        
        if n % 2 != 0:
            return float(merged_arr[n // 2])
        else:
            return float((merged_arr[int((n -1)/2)] + merged_arr[int(n/2)])/2.0)
        
    def merge(self, arr_1, arr_2):
        i = j = 0
        merged_arr = []
        while i < len(arr_1) and j < len(arr_2):
            if arr_1[i] < arr_2[j]:
                merged_arr.append(arr_1[i])
                i += 1
            else:
                merged_arr.append(arr_2[j])
                j += 1
        
        # copy the remaing elements to the merged_arr
        while i < len(arr_1):
            merged_arr.append(arr_1[i])
            i += 1
            
        while j < len(arr_2):
            merged_arr.append(arr_2[j])
            j += 1
        
        return merged_arr