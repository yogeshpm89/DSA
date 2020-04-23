from LinkedList import LinkedList


def divideList(list):
    temp = list.head
    head1 = temp
    head2 = list.head
    tail = None

    while temp.next != None:
        temp = temp.next
        if temp.next != None:
            temp = temp.next
        tail = head2
        head2 = head2.next

    list1 = LinkedList()
    list2 = None
    if tail != None:
        tail.next = None
        list1 = LinkedList()
        list2 = LinkedList()

        while head1 != None:
            list1.insertNodeAtLast(head1.data)
            head1 = head1.next

        while head2 != None:
            list2.insertNodeAtLast(head2.data)
            head2 = head2.next

    return (list1, list2)


def sort(llist):
    if llist == None:
        return
    if llist.head == None:
        return

    lArray = divideList(llist)
    list1 = lArray[0]
    list2 = lArray[1]
    if list1.head.next != None:
        list1 = sort(list1)
    if list2.head.next != None:
        list2 = sort(list2)

    return mergeLists(list1, list2)


def mergeLists(list1, list2):
    list3 = LinkedList()
    temp1 = None
    temp2 = None
    if list1 != None:
        temp1 = list1.head
    if list2 != None:
        temp2 = list2.head

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
sortedList = sort(llist)
printList(sortedList)
