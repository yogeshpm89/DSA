import math


def sort(a, low, pivot, high):
    if (low >= pivot):
        return
    pivot = quickSort(a, low, pivot)
    sort(a, low, pivot)
    sort(a, pivot+1, high)


def quickSort(a, low, high):
    counter = low
    for i in range(low, high):
        if (a[i] > pivot):
            swap(a, i, i+1)
            counter = counter + 1
    swap(a, counter, high)
    return counter

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

a = [6,5,4,3,2,1,8,0]
sort(a, 0, 7)
print(a)