def generate_numbers(N, M, prefix=None):
    """Генерирует числа с лидирующими незначащами нулями
       в N-ричной системе счисления, при N <= 10
       длины М
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()

def check_for_previous_instance(number, A):
    """ищет x в А и возвращает True если такой есть
       и False если такого нет
    """
    for x in A:
        if number == x:
            return True
    return False

def generate_permutaions(N:int, M:int=-1, prefix=None):
    """Генерирует всех перестановок N чисел в М позициях,
       с префиксом prefix
    """
    M = M if M != -1 else N # по умолчанию N чисел N позициях
    prefix = prefix or []
    if M == 0:
        print(*prefix, sep='')
        return
    for number in range(1, N+1):
        if check_for_previous_instance(number, prefix):
            continue
        prefix.append(number)
        generate_permutaions(N, M-1, prefix)
        prefix.pop()


generate_permutaions(4, 4)