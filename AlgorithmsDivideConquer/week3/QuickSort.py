
def partition(A, l, r):
    if len(A) <= 1:
        return A

    p = A[l]
    i = l+1
    for j in range(l+1, r):
        if A[j] < p:
            tmp = A[j]
            A[j] = A[i]
            A[i] = tmp
            i += 1
    tmp = A[l]
    A[l] = A[i-1]
    A[i-1] = tmp
    return A, i-1

def quickSort(A):
    if len(A) <= 1:
        return A, 0

    n = len(A)

    comparisons = n-1

    p = 0 #pivot1 162085
    p = n-1 #pivot 2 164123


    #pivot3

    l = 0
    m = 0
    if n % 2 > 0:
        m = n//2
    else:
        m = n//2 - 1
    r = n-1

    a1 = A[l]
    a2 = A[m]
    a3 = A[r]
    if (a1 > a2 and a1 < a3) or (a1 < a2 and a1 > a3):
        p = l
    elif (a2 > a1 and a2 < a3) or (a2 < a1 and a2 > a3):
        p = m
    else:
        p = r


    if p != 0:
        tmp = A[0]
        A[0] = A[p]
        A[p] = tmp
        p = 0

    sA, l = partition(A.copy(), p, n)
    L = sA[:l]
    R = sA[l+1:]
    sL, cl = quickSort(L)
    sR, cr = quickSort(R)

    return sL + [A[p]] + sR, comparisons + cl + cr

text_file = open("QuickSort.txt", "r")
lines = text_file.readlines()
arr = list(map(int, lines))

#arr = [4, 5, 6, 7]
qs, cm = quickSort(arr)
print(cm)