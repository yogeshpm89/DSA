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
        output = ""
        while (temp):
            output = output + str(temp.data) + "  "
            temp = temp.next
        print(output)
        print("*******************************************************")

    def printListRec(self, head):
        if (head == None):
            return
        print(head.data)
        self.printListRec(head.next)

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

    def swapNodes(self, x, y):
        if x == y:
            return

        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        if prevX == None:
            self.head = currY
        else:
            prevX.next = currY

        if prevY == None:
            self.head = currX
        else:
            prevY.next = currX

        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def reverse(self):
        last = None
        curr = self.head
        prev = None
        while curr != None:
            prev = curr
            curr = curr.next
            prev.next = last
            last = prev
        self.head = prev
