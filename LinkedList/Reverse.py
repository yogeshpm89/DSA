from LinkedList import LinkedList


def reverseList(head):
    curr = head
    last = None
    while curr != None:
        nextNode = curr.next
        curr.next = last
        last = curr
        curr = nextNode
    return last


def reverseListInBatches(head, k):
    if head == None:
        return
    curr = head
    last = None
    nextNode = None
    count = 0
    while curr != None and count < k:
        nextNode = curr.next
        curr.next = last
        last = curr
        curr = nextNode
        count = count + 1

    if nextNode is not None:
        head.next = reverseListInBatches(nextNode, k)
    return last


llist = LinkedList()
for i in range(1, 6):
    llist.insertNodeAtLast(i)
llist.printList()
llist.head = reverseListInBatches(llist.head, 3)
llist.printList()
