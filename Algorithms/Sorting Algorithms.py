def insert_sort(A):
    n = len(A)
    for top in range(1, n):
        k = top
        while k < 0 and A[k] < A[k - 1]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1


def choice_sort(A):
    n = len(A)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    n = len(A)
    for bypass in range(1, n):
        for k in range(0, bypass-1):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
