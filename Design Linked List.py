class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        return

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        i = 0
        node = self.head
        while node != None:
            if i==index:
                return node.val
            node = node.next
            i += 1
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            secondNode = self.head
            node = Node(val)
            self.head = node
            node.next = secondNode
            
        return
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.head == None:
            self.head = Node(val)
            self.tail = self.head
        else:
            node = Node(val)
            self.tail.next = node
            self.tail = node
            
        return
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if(index == 0 and self.head == None):
            self.head = Node(val)
            self.tail = self.head
            return
        i = 0
        node = self.head
        while node != None:
            if i==index-1:
                newNode = Node(val)
                newNode.next = node.next
                node.next = newNode
                if newNode.next == None:
                    self.tail = newNode
                return
            node = node.next
            i += 1
        return
                
        

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        i = 0
        node = self.head
        while node.next != None:
            if i==index-1:
                if node.next.next == None:
                    self.tail = node
                node.next = node.next.next
                return
            node = node.next
            i += 1
        return
    
    def printList(self):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        node = self.head
        if self.head != None:
            print("head: " + str(self.head.val))
            print("tail: " + str(self.tail.val))
        print('|')
        while node != None:
            print(node.val)
            node = node.next
        print('|')
        print()
        return


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)