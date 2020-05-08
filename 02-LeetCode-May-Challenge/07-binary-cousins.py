# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.pX = 0
        self.pY = 0
        self.dX = -1
        self.dY = -1
        
        self.parent_and_depth(root, x, y, 0)
        return ((self.dX == self.dY) and (self.pX != self.pY))
    
    def parent_and_depth(self, root: TreeNode, x: int, y: int, d: int) -> bool:
        if root == None:
            return
        if root.left != None:
            if root.left.val == x:
                self.pX = root.val
                self.dX = d + 1
            elif root.left.val == y:
                self.pY = root.val
                self.dY = d + 1
        
        if root.right != None:
            if root.right.val == x:
                self.pX = root.val
                self.dX = d + 1
            elif root.right.val == y:
                self.pY = root.val
                self.dY = d + 1
        
        if (self.dX != -1 and self.dY != -1):
            return
        
        self.parent_and_depth(root.left, x, y, d+1)
        self.parent_and_depth(root.right, x, y, d+1)

####################################
######### Faster Solution ##########
####################################
class Solution_opt:
    def isCousins_opt(self, root: TreeNode, x: int, y: int) -> bool:
        
        
        def depth(root,x,par,level):
            if not root:
                return 
            
            if root.val==x:
                return [level,par]
            
            return depth(root.left,x,root,level+1) or depth(root.right,x,root,level+1)
        
        a=depth(root,x,None,1)
        b=depth(root,y,None,1)
        if a[0]==b[0] and a[1]!=b[1]:
            return True
        return False