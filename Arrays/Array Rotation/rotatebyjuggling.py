import time

def gcd_euclid(a, b):
    if a==b:
        return a
    elif a > b:
        return gcd_euclid(a-b, b)
    elif a < b:
        return gcd_euclid(a, b-a)

def gcd_steins(a, b):
    if a==b:
        return a
    elif a%2==0 and b%2==0:
        return gcd_steins(a/2, b/2)
    elif a%2==0:
        return gcd_steins(a/2, b)
    elif b%2==0:
        return gcd_steins(a, b/2)
    elif a > b:
        return gcd_steins(a-b, b)
    elif a < b:
        return gcd_steins(a, b-a)



def rotateArrLeft(arr, d):
    n = len(arr)
    split_point = d%n
    gcd = gcd_steins(d, n)

    for i in range(split_point):
        rotateByGCD(arr, n, gcd)

def rotateByGCD(arr, n, gcd):
    temp = arr[i]
    for i in range(n, step=gcd):
        arr[i] = arr[i+split_point]

arr = [1, 2, 3, 4, 5]

def rotateArrLeft2(arr, d):
    n = len(arr)
    k = d % n
    for i in range(n-k):
        temp = arr[i]
        arr[i] = arr[i + k]
        arr[i+k] = temp
    if n%2 != 0:
        temp = arr[n-2]
        arr[n-2] = arr[n-1]
        arr[n-1] = temp
    print(arr)


rotateArrLeft2(arr, 4)
