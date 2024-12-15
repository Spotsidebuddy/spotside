def matryoshka(n):
    if n == 1:
        print('матрёшечка')
    else:
        print('верх матрешки n =', n)
        matryoshka(n-1)
        print('низ матрешки n =', n)


matryoshka(5)