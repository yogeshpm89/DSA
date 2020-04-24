from LinkedList import LinkedList


def rotateList(llist, k):
    head = llist.head
    kNode = None
    curr = head
    k1Node = None
    count = 1
    while curr != None and count < k:
        curr = curr.next
        count = count + 1
    if curr is not None and curr.next is not None:
        kNode = curr
        k1Node = curr.next
    else:
        return llist

    while curr.next != None:
        curr = curr.next

    kNode.next = None
    curr.next = head
    llist.head = k1Node
    return llist


llist = LinkedList()
for i in range(1, 3):
    llist.insertNodeAtLast(i)
llist.printList()

llist = rotateList(llist, 1)
llist.printList()
