from LinkedList import LinkedList

def mergeLists(list1, list2):
    outputHead = None
    curr1 = list1.head
    curr2 = list2.head
    
    if (curr1.data < curr2.data):
        outputHead = list1
        curr1 = curr1.next
    else:
        outputHead = list2
        curr2 = curr2.next

    last = outputHead.head
    while curr1 != None or curr2 != None:
        if curr1 == None:
            last.next = curr2
            last = curr2
            curr2 = curr2.next
            continue

        if curr2 == None:
            last.next = curr1
            last = curr1
            curr1 = curr1.next
            continue

        if (curr1.data < curr2.data):
            last.next = curr1
            last = curr1
            curr1 = curr1.next
        else:
            last.next = curr2
            last = curr2
            curr2 = curr2.next
    return outputHead

list1 = LinkedList()
list1.insertNodeAtLast(2)
list1.insertNodeAtLast(5)
list1.insertNodeAtLast(10)
list1.insertNodeAtLast(15)

list2 = LinkedList()
list2.insertNodeAtLast(2)
list2.insertNodeAtLast(3)
list2.insertNodeAtLast(20)

list3 = mergeLists(list1, list2)
list3.printList()
            



    