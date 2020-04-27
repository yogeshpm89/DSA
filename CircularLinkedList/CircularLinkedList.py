
from Node import Node


class CircularLinkedList:

    def __init__(self):
        self.last = None

    def insertNode(self, data):
        newNode = Node(data)
        last = self.last
        if last == None:
            last = newNode
            newNode.next = newNode
            self.last = newNode
            return

        head = last.next
        last.next = newNode
        newNode.next = head
        self.last = newNode

    def print(self):
        last = self.last
        if last is None:
            print("List is empty")
            return

        temp = last.next
        output = ""
        while temp != last:
            output = output + str(temp.data) + " "
            temp = temp.next
        output = output + str(temp.data) + " "
        print("*******************************************************************")
        print(output)
        print("*******************************************************************")
