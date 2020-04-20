from Node import Node
# Linked List class 
class LinkedList: 
     
    # Function to initialize the Linked  
    # List object 
    def __init__(self):  
        self.head = None

    # This function prints contents of linked list 
    # starting from head 
    def printList(self):
        print("*******************************************************")
        temp = self.head 
        while (temp):
            print(temp.data)
            temp = temp.next
        print("*******************************************************")

    def insertNodeAtStart(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertNodeAfter(self, prevNode, data):
        newNode = Node(data)
        temp = self.head
        while temp != None and temp.data != prevNode:
            temp = temp.next
        
        newNode.next = temp.next
        temp.next = newNode

    def insertNodeAtLast(self, data):
        newNode = Node(data)
        temp = self.head

        if temp == None:
            self.head = newNode
            return
        
        while temp.next != None:
            temp = temp.next
        temp.next = newNode

    def deleteNode(self, data):
        temp = self.head

        if (temp.data == data):
            self.head = temp.next
            return

        while temp.next != None and temp.next.data != data:
            temp = temp.next
        
        temp.next = temp.next.next

    def deleteNodeAtPosition(self, index):
        count = 1
        temp = self.head

        if index == 0:
            self.head = self.head.next

        while count < index-1:
            temp = temp.next
            count = count + 1
        
        if temp == None:
            return
        if temp.next == None:
            return
            
        temp.next = temp.next.next