import math


def sort(a, low, high):
    if (low >= high):
        return
    mid = math.floor((low + high) / 2)
    sort(a, low, mid)
    sort(a, mid + 1, high)
    merge(a, low, mid, high)

def merge(a, low, mid, high):
    aux = []
    for i in range(0, len(a)):
        aux.append(a[i])
    i = low
    j = mid + 1
    k = low
    for k in range(low, high+1):
        if i > mid:
            a[k] = aux[j]
            j = j + 1
        elif j > high:
            a[k] = aux[i]
            i = i + 1
        elif aux[i] <= aux[j]:
            a[k] = aux[i]
            i = i + 1
        else:
            a[k] = aux[j]
            j = j + 1

a = [6,5,4,3,2,1,8,0]
sort(a, 0, 7)
print(a)