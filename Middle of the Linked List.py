# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        currentNode = head
        listLength = 0
        while currentNode != None:
            listLength += 1
            currentNode = currentNode.next
            
        currentNode = head
        for i in range(listLength//2):
            currentNode = currentNode.next
        
        
        return currentNode