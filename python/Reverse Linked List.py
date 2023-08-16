# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.recurse(head, None)
    
    def recurse(self, current_node, new_head):
        if current_node == None:
            return new_head
        else:
            temp = current_node.next
            current_node.next = new_head
            new_head = current_node
            current_node = temp
            return self.recurse(current_node, new_head)