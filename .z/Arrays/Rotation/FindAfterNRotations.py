"""
@github: github.com/alikhalilli

[1, 2, 3, 4, 5]
[3, 1, 2, 4, 5]
[4, 3, 1, 2, 5]

ranges = [(0, 2), (0, 3)]
Method : Efficient 
We can do offline processing after saving all ranges.
Suppose, our rotate ranges are : [0..2] and [0..3]
We run through these ranges from reverse.

[left, right]
After range [0..3], index 0 will have the element which was on index 3. [index == left => index=right]
So, we can change 0 to 3, i.e. if index = left, index will be changed to right. [index == left => index=right]
After range [0..2], index 3 will remain unaffected.

So, we can make 3 cases :
If index = left, index will be changed to right.
If index is not bounds by the range, no effect of rotation.
If index is in bounds, index will have the element at index-1. [at each rotation]
"""
ranges = [(0, 2), (0, 3)]
arr = [1, 2, 3, 4, 5]


def findElement(arr, ranges):
    rotations = len(ranges)
    index = 1
    # run through ranges from reverse.
    for i in range(rotations-1, -1, -1):
        left, right = ranges[i]

        if (left <= index and index <= right):
            if (index == left):
                index = right
            else:
                index -= 1
    return arr[index]


print(findElement(arr, ranges))
