def check_sorted(A, ascending=True):
    """проверка отсортированности за О(len(A))"""
    # int от True возвращает 1
    # a от False возвращает 0
    # чтобы сдеать -1 от False
    # и сохранить 1 от True
    # делаем мат функцию
    # s = 2*int(True) - 1 = 2 * 1 - 1 = 1
    # s = 2*int(False) - 1 = 2 * 0 - 1 = -1
    flag = True
    n = len(A)
    s = 2 * int(ascending) - 1
    for i in range(0, n - 1):
        if s * A[i] > s * A[i + 1]:
            flag = False
    return flag
