from LinkedList import LinkedList

llist = LinkedList()
for i in range(1, 10):
    llist.insertNodeAtLast(i)
llist.printList()
llist.reverseInBatches(llist.head, 3)
llist.printList()
