def fac(n: int):
    """ФАКТОРИАЛ ЧИСЛА n"""
    assert n > 0
    if n <= 1:
        return 1
    else:
        return fac(n - 1) * n


def gcd_1(a, b):
    """АЛГОРИТМ ЕВКЛИДА
    нахождение наибольшего общего делителя
    GreatestCommonDenomenator
    СПОСОБ НОМЕР 1 (неоптимизированный)"""
    if a == b:
        return a
    elif a > b:
        return gcd_1(a - b, b)
    else:  # остается только случай a < b
        return gcd_1(a, b - a)


def gcd_2(a, b):
    """АЛГОРИТМ ЕВКЛИДА
    нахождение наибольшего общего делителя
    GreatestCommonDenomenator
    СПОСОБ НОМЕР 2 (оптимизированный)"""
    if b == 0:
        return a
    return gcd_2(b, a % b)
    # return a if b == 0 else gcd_2(b, a % b) - запись тернарным оператором


def quick_pow_1(a: float, n: int):
    """БЫСТРОЕ ВОЗВЕДЕНИЕ В СТЕПЕНЬ
        СПОСОБ 1(неоптимизированный)"""
    if n == 0:
        return 1
    else:
        return quick_pow_1(a, n - 1) * a


def quick_pow_2(a, n):
    """БЫСТРОЕ ВОЗВЕДЕНИЕ В СТЕПЕНЬ
        СПОБОБ 2 (оптимизированный)"""
    if n == 0:
        return 1
    elif n % 2 == 1:
        return quick_pow_2(a, n - 1) * a
    else:
        return quick_pow_2(a**2, n // 2)


print(quick_pow_2(4, 100))