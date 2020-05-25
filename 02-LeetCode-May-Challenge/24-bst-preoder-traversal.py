# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert(root, val):
    """
    a utility func to add data to the tree
    """
    if root is not None:
        if val>root.val:
            if root.right is not None:
                insert(root.right, val)
            else:
                root.right = TreeNode(val)
        else:
            if root.left is not None:
                insert(root.left, val)
            else:
                root.left = TreeNode(val)
    
class Solution:
    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder[0])
        for i in range(1, len(preorder)):
            insert(root, preorder[i])
        
        return root