# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sumDigit, carry = self.addWithCarry(l1.val, l2.val, 0)
        head = ListNode(sumDigit)
        nodeOut = head
        nodeL1 = l1.next
        nodeL2 = l2.next

        while (nodeL1 != None) or (nodeL2 != None) or (carry != 0):
            if (nodeL1 == None) and (nodeL2 == None) and (carry != 0):
                sumDigit, carry = self.addWithCarry(0, 0, carry)
            elif nodeL1 == None:
                sumDigit, carry = self.addWithCarry(0, nodeL2.val, carry)
                nodeL2 = nodeL2.next
            elif nodeL2 == None:
                sumDigit, carry = self.addWithCarry(nodeL1.val, 0, carry)
                nodeL1 = nodeL1.next
            else:
                sumDigit, carry = self.addWithCarry(nodeL1.val, nodeL2.val, carry)
                nodeL1 = nodeL1.next
                nodeL2 = nodeL2.next
                
            nodeOut.next = ListNode(sumDigit)
            nodeOut = nodeOut.next
            
        return head
                
        
    def addWithCarry(self, a, b, carry):
        sumDigit = (a+b+carry)%10
        carry = (a+b+carry)//10
        return sumDigit, carry