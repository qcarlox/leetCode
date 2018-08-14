# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        nodesAtHeight = self.treeHelper(root, {}, 1)
        maxHeight = 0
        for height in nodesAtHeight:
            maxHeight = max(maxHeight, height)
        
        
        return nodesAtHeight[maxHeight][0]
    
    def treeHelper(self, root, nodesAtHeight, height):
        if root is None:
            return nodesAtHeight
        if height in nodesAtHeight:
            nodesAtHeight[height].append(root.val)
        else:
            nodesAtHeight[height] = [root.val]
        height += 1
        nodesAtHeight = self.treeHelper(root.left, nodesAtHeight, height)
        nodesAtHeight = self.treeHelper(root.right, nodesAtHeight, height)
        return nodesAtHeight