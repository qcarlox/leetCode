# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        
            
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        
        if root.left == None and root.right == None:
            if root.val == 1:
                return root
            else:
                return None
        
        return root