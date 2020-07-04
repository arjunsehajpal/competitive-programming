# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root, depth = 0):
        if root is None:
            return depth
        else:
            depth = depth + 1
            left_depth = self.maxDepth(root.left, depth = depth)
            right_depth = self.maxDepth(root.right, depth = depth)
            
            if left_depth >= right_depth:
                return left_depth
            else:
                return right_depth