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

    llist.printListRec(llist.head)

    llist.insertNodeAtLast(5)
    llist.insertNodeAtLast(6)
    llist.insertNodeAtLast(7)
    llist.insertNodeAtLast(8)
    llist.insertNodeAtLast(9)
    llist.insertNodeAtLast(10)

    llist.printList()

    llist.swapNodes(5, 9)
    llist.printList()

    llist.swapNodes(7, 8)
    llist.printList()

    llist.swapNodes(1, 2)
    llist.printList()

    llist.reverse()
    llist.printList()

    llist1 = LinkedList()
    llist1.insertNodeAtLast(1)
    llist1.reverse()
    llist1.printList()

    