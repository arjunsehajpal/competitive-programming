class Solution:
    def intervalIntersection(self, A, B):
        result = []
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            a = A[i]
            b = B[j]
            if a[1] < b[0]:
                i += 1
            elif b[1] < a[0]:
                j += 1
            else:
                start = max(a[0], b[0])
                end = min(a[1], b[1])
                result.append([start, end])
                if a[1] < b[1]:
                    i += 1
                elif a[1] >= b[1]:
                    j += 1
        return result