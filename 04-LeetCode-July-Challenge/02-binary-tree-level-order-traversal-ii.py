# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root):
        resultant_list = []
        if root == None:
            return resultant_list
        
        queue = []
        queue.append(root)
        while len(queue) > 0:
            nodes = []
            for i in range(0, len(queue)):
                node = queue.pop(0)
                nodes.append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            resultant_list.insert(0, nodes)
        return resultant_list