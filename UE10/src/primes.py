"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "0.1"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "In Progress"
"""

import itertools
import math

def is_prime(n, known_primes):
    """Prüft, ob eine Zahl eine Primzahl ist, basierend auf bekannten Primzahlen."""
    if n <= 1:
        return False
    for prime in known_primes:
        if prime * prime > n:
            break
        if n % prime == 0:
            return False
    return True

def primesCached(known_primes=[2, 3, 5]):
    """Generator, der Primzahlen liefert, beginnend mit einer Liste bekannter Primzahlen."""
    yield from known_primes
    number = known_primes[-1] + 2
    while True:
        if is_prime(number, known_primes):
            known_primes.append(number)
            yield number
        number += 2

def nth_prime(n, generator):
    """Bestimmt die n-te Primzahl mithilfe eines Generators."""
    prime_gen = generator()
    prime = next(prime_gen)
    for _ in range(n - 1):
        prime = next(prime_gen)
    return prime

# Erste 100 Primzahlen ausgeben
first_100_primes = list(itertools.islice(primesCached(), 100))
print(first_100_primes)

# Alle Primzahlen bis 100.000 ausgeben
for prime in primesCached():
    if prime > 100000:
        break
    print(prime, end=' ')

# Zeit für die 200.000-te Primzahl
import time

start_time = time.time()
prime_200000 = nth_prime(200000, primesCached)
end_time = time.time()
print(f"\n200000-te Primzahl: {prime_200000}, Zeit: {end_time - start_time} Sekunden")

# Zeit für die 400.000-te Primzahl
start_time = time.time()
prime_400000 = nth_prime(400000, primesCached)
end_time = time.time()
print(f"400000-te Primzahl: {prime_400000}, Zeit: {end_time - start_time} Sekunden")
