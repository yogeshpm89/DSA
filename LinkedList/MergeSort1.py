from LinkedList import LinkedList


def getMiddleNode(head):
    slowPointer = head
    fastPointer = head

    while fastPointer.next != None:
        fastPointer = fastPointer.next
        if fastPointer.next != None:
            fastPointer = fastPointer.next
        slowPointer = slowPointer.next
    return slowPointer


def sort(head):
    if head == None:
        return
    if head.next == None:
        return

    middle = getMiddleNode(head)
    nextToMiddle = middle.next

    list1 = sort(middle)
    list2 = sort(nextToMiddle)

    return mergeLists(list1, list2)


def mergeLists(node1, node2):
    list3 = LinkedList()
    temp1 = node1
    temp2 = node2
    while temp1 != None or temp2 != None:
        if (temp1 == None):
            list3.insertNodeAtLast(temp2.data)
            temp2 = temp2.next
            continue
        if (temp2 == None):
            list3.insertNodeAtLast(temp1.data)
            temp1 = temp1.next
            continue
        if (temp1.data < temp2.data):
            list3.insertNodeAtLast(temp1.data)
            temp1 = temp1.next
        else:
            list3.insertNodeAtLast(temp2.data)
            temp2 = temp2.next
    return list3


def printList(list):
    if list == None:
        return
    head = list.head
    output = ""
    while head != None:
        output = output + str(head.data) + " -> "
        head = head.next
    print(output)


llist = LinkedList()
llist.insertNodeAtLast(5)
llist.insertNodeAtLast(32)
llist.insertNodeAtLast(31)
llist.insertNodeAtLast(7)
llist.insertNodeAtLast(1)
llist.insertNodeAtLast(8)
llist.insertNodeAtLast(3)
llist.insertNodeAtLast(4)
llist.insertNodeAtLast(9)
printList(llist)
sortedList = sort(llist.head)
printList(sortedList)
