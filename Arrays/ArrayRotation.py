a = [1, 2, 3, 4, 5, 6, 7]
def rotate_arr(a,d):
    n=len(a)
    b = []
    for x in range(d, n):
        b.append(a[x])
    for k in range(0, d):
        b.append(a[k])
    print(b)

rotate_arr(a, 1)
