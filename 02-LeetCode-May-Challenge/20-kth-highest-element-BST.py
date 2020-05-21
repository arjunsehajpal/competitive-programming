# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k) -> int:
        self.count = 0
        self.result = 0
        self.kth_inorder(root, k)
        return self.result
    
    def kth_inorder(self, root, k):
        if root.left != None:
            self.kth_inorder(root.left, k)
        self.count += 1
        if self.count == k:
            self.result = root.val
            return
        
        if root.right != None:
            self.kth_inorder(root.right, k)