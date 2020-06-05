# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root):
        if root == None:
            return
        else:
            temp = root
            
            # recurse the function on the subtrees
            self.invertTree(root.left)
            self.invertTree(root.right)
            
            # swapping
            temp = root.left
            root.left = root.right
            root.right = temp
        
        return root