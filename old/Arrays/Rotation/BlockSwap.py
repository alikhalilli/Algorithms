"""
@github: github.com/alikhalilli
Time Complexity: O(n)

[1, 2, 3, 4, 5, 6, 7] => [3, 4, 5, 6, 7, 1, 2]

i = d => 2 len(A)
j = n-d => 5 len(B)

while i!=j:
    if i < j:
        [[1, 2], 3, 4, 5, [6, 7]]
        SWAP A and Br
        [6, 7, 3, 4, 5, | 1, 2]
        j = j - i => 3 (new_len(B) = old_len(B) - old_len(A))
    
        [[6, 7], 3, [4, 5], | 1, 2]
        SWAP new-A and Br
        [4, 5, 3, | 6, 7, 1, 2]
        j = j - i => 3 - 2 => 1 (new_len(B))
    if i > j:
        SWAP new-A(si=d-i, fi=d, j)
        [[4], 5, [3], | 6, 7, 1, 2]
"""


def swap(arr, fi, si, d):
    for i in range(d):
        temp = arr[fi + i]
        arr[fi + i] = arr[si + i]
        arr[si + i] = temp


def rotate(arr, d):
    size = len(arr)
    if d == 0 or size == d:
        return
    sizeA = d
    sizeB = size - d
    while sizeA != sizeB:
        # A is shorter than B
        if sizeA < sizeB:
            swap(arr, d-sizeA, d+sizeB-sizeA, sizeA)
            sizeB = sizeB - sizeA
        # B is shorter than A
        else:
            swap(arr, d-sizeA, d, sizeB)
            sizeA = sizeA - sizeB
    swap(arr, d-sizeA, d, sizeA)
