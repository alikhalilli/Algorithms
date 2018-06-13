"""
@github: github.com/alikhalilli

arr = [1, 2, 3, 4, 5]
ranges = [(0, 2), (0, 3)]
Method : Efficient 
We can do offline processing after saving all ranges.
Suppose, our rotate ranges are : [0..2] and [0..3]
We run through these ranges from reverse.

After range [0..3], index 0 will have the element which was on index 3.
So, we can change 0 to 3, i.e. if index = left, index will be changed to right.
After range [0..2], index 3 will remain unaffected.

So, we can make 3 cases :
If index = left, index will be changed to right.
If index is not bounds by the range, no effect of rotation.
If index is in bounds, index will have the element at index-1.
"""
ranges = [(0, 2), (0, 3)]
arr = [1, 2, 3, 4, 5]


def findElement(arr, ranges, d, index):
    for i in range(d-1, -1, -1):
        left, right = ranges[i]

        if (left <= index and right >= index):
            if (index == left):
                index = right
            else:
                index -= 1
    return arr[index]
