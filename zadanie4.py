# 
# Poniżej znajdują się dwie funkcje obliczające sumę liczb
# pierwszych do N. Pierwsza używa naiwnego algorytmu, druga –
# Sita Eratostenesa.
#
# Polecenia:
#   1. Wybierz JEDNĄ z dwóch wcześniej omówionych metod:
#        a) time.time() – zmierz czas wykonania każdej funkcji
#           ręcznie i wypisz wyniki w sekundach,
#      LUB
#        b) cProfile – uruchom profilowanie obu funkcji
#           i wyświetl raport (użyj `cProfile.run(...)` lub
#           `pstats`).
#   2. Dla N = 500_000 porównaj czasy obu funkcji.
# 
 
import cProfile  
import time
 
 
def sum_primes_naive(n: int) -> int:
    """Naiwna metoda – sprawdza każdą liczbę z osobna."""
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
 
    return sum(x for x in range(2, n + 1) if is_prime(x))
 
 
def sum_primes_sieve(n: int) -> int:
    """Sito Eratostenesa."""
    if n < 2:
        return 0
    sieve = bytearray([1]) * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    return sum(i for i, v in enumerate(sieve) if v)
 
 
N = 500_000
 

 
 
