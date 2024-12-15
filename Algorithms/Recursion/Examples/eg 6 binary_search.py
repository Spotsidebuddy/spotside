A = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5, 7, 7, 7, 7]


def left_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] < key:
            left = mid
        else:
            right = mid
    return left


def right_bound(A, key):
    left = -1
    right = len(A)
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] <= key:
            left = mid
        else:
            right = mid
    return right

def binary_search(A, key):
    left = left_bound(A, key)
    right = right_bound(A, key)
    return left, right

print(binary_search(A, 7))
print(len(A))