arr = [4, 5, 6, 7, 1, 2, 3]
x = 7


def pairInSortedRotated(arr, n, x):
    for i in range(n - 1):
        if (arr[i] > arr[i + 1]):
            break
    l = int((i + 1) % n)  # index of minimum element
    r = i  # index of maximum element
    results = []
    print("minimum: ", arr[l], "\nmaximum: ", arr[r])
    while l != r:
        if arr[l] + arr[r] == x:
            results.append((arr[l], arr[r]))
            return (True, results)

        if arr[l] + arr[r] < x:
            l = (l + 1) % n
        else:
            r = (n + r - 1) % n
    return (False, results)

print(pairInSortedRotated(arr, len(arr), 5)[1])
