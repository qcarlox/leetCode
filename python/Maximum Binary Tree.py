# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        
        maxNum = max(nums)
        maxNumIndex = nums.index(maxNum)
        currentNode = TreeNode(maxNum)
        leftList = nums[0:maxNumIndex]
        rightList = nums[maxNumIndex+1:]
        currentNode.right = self.constructMaximumBinaryTree(rightList)
        currentNode.left = self.constructMaximumBinaryTree(leftList)
        return currentNode