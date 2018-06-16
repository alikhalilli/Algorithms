
def mergeSort(arr, l, r):
    if l < r:
        m = int(l + (l-r)/2)
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    i = 0
    j = 0
    k = l
