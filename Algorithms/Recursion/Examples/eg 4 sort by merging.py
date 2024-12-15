"""СОРТИРОВКА СЛИЯНИЕМ"""
"""БЕЗ РЕКУРСИИ"""


def merge(A, B):
    i = k = n = 0
    C = [0] * len(A + B)
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1
    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1
    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1
    return C


"""С РЕКУРСИЕЙ"""


def sort_merge_recursive(A):
    if len(A) <= 1:
        return
    mid = len(A) // 2
    L = [A[i] for i in range(0, mid)]
    R = [A[i] for i in range(mid, len(A))]
    sort_merge_recursive(L)
    sort_merge_recursive(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]
    return A


B = [5, 2, 7, 3, 1]

print(sort_merge_recursive(B))
