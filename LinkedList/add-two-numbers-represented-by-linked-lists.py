from LinkedList import LinkedList


def addList(list1, list2):
    curr1 = list1.head
    curr2 = list2.head
    data1 = 0
    data2 = 0
    data3 = 0
    carry = 0
    output = LinkedList()
    while curr1 != None or curr2 != None:
        data1 = 0
        data2 = 0
        if curr1 != None:
            data1 = curr1.data
            curr1 = curr1.next
        if curr2 != None:
            data2 = curr2.data
            curr2 = curr2.next
        data3 = (data1 + data2 + carry) % 10
        carry = int((data1 + data2 + carry) / 10)
        output.insertNodeAtLast(data3)
    if carry > 0:
        output.insertNodeAtLast(carry)
    return output


# llist1 = LinkedList()
# llist1.insertNodeAtLast(5)
# llist1.insertNodeAtLast(6)
# llist1.insertNodeAtLast(3)

# llist2 = LinkedList()
# llist2.insertNodeAtLast(8)
# llist2.insertNodeAtLast(4)
# llist2.insertNodeAtLast(2)

# llist1.printList()
# llist2.printList()

# llist3 = addList(llist1, llist2)
# llist3.printList()

llist4 = LinkedList()
llist4.insertNodeAtLast(7)
llist4.insertNodeAtLast(5)
llist4.insertNodeAtLast(9)
llist4.insertNodeAtLast(4)
llist4.insertNodeAtLast(6)

llist5 = LinkedList()
llist5.insertNodeAtLast(8)
llist5.insertNodeAtLast(4)

llist4.printList()
llist5.printList()

llist6 = addList(llist4, llist5)
llist6.printList()
