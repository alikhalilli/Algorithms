# @akhalilli 2020


"""
Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements.


Using Temp Array:

Space Complexity: O(d)
Time Complexity: O(n)

Left Rotation:
arr = [1, 2, 3, 4, 5]
d=2
split_point = d%len(arr)
temp = arr[:split_point]
arr[:split_point] = arr[split_point:-1]
arr[split_point:-1] = temp
[3, 4, 5, 1, 2]


arr = [1, 2, 3, 4, 5]
d=7 => [3, 4, 5, 1, 2]

Right Rotation:
arr = [1, 2, 3, 4, 5]
d=2 => [3, 4, 5, 1, 2]
arr = [1, 2, 3, 4, 5]
d=7 => [3, 4, 5, 1, 2]
"""



def rotateLeft(arr, d):
    n = len(arr)
    split_point = d%n
    temp_arr = list()

    for i in range(split_point):
        temp_arr.append(arr[i])
    
    for i in range(n-split_point):
        arr[i] = arr[i+split_point]

    for i in range(split_point):
        arr[n-split_point+i] = temp_arr[i]

    return arr

def rotateRight(arr, d):
    n = len(arr)
    split_point = d%n

    temp_arr = [None]*split_point

    for i in range(split_point):
        temp_arr[i] = arr[n-split_point+i]
    
    for i in range(n,split_point,-1):
        arr[i-1] = arr[i-split_point-1]
    
    for i in range(split_point):
        arr[i] = temp_arr[i]
    print(arr)
    

arr = [1, 2, 3, 4, 5]

#print(rotateLeft(arr, 2))
rotateRight(arr, 25)