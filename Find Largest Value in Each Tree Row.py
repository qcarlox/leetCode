# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nodesAtHeight = self.treeHelper(root, [] , 1)
            
        return nodesAtHeight
        
    def treeHelper(self, node, nodesAtHeight, height):
        if node is None:
            return nodesAtHeight
        if len(nodesAtHeight) >= height:
            nodesAtHeight[height-1] = max(nodesAtHeight[height-1], node.val)
        else:
            nodesAtHeight.append(node.val)
        height += 1
        
        nodesAtHeight = self.treeHelper(node.left, nodesAtHeight, height)
        nodesAtHeight = self.treeHelper(node.right, nodesAtHeight, height)
        
        return nodesAtHeight
        