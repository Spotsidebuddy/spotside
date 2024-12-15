

def print_primes_up_to(n):
    A = [True] * (n+1)
    A[0] = A[1] = False

    for k in range(2, n):
        if A[k]:
            for m in range(2*k, n, k):
                A[m] = False
    for k in range(n):
        print(k, '-', 'простое' if A[k] else 'составное')

print_primes_up_to(2500)