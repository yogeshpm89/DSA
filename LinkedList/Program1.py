from LinkedList import LinkedList
from Node import Node

# Code execution starts here 
if __name__=='__main__': 
  
    # Start with the empty list 
    llist = LinkedList() 
  
    llist.head = Node(1) 
    second = Node(2) 
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printList()

    llist.insertNodeAtStart(0)

    llist.printList()

    llist.insertNodeAfter(2, 2.5)

    llist.printList()

    llist.insertNodeAtLast(4)

    llist.printList()

    llist.deleteNode(0)

    llist.printList()

    llist.deleteNodeAtPosition(6)

    llist.printList()