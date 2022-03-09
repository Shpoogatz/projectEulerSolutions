# Euler 10
# this is my solution to Project Euler 10

from math import isqrt

# Sieve of Eratosthenes
# https://github.com/Shpoogatz/usefulThings/blob/main/sieveOfEratosthenes.py
def primesLessThan(input):
    if input <= 2:
        return []
    primes = [True] * input
    primes[0] = False
    primes[1] = False

    for i in range(2,isqrt(input)):

        if primes[i]:
            for j in range(i*i, input, i):
                primes[j] = False
    return [i for i in range(input) if primes[i]]

print(sum(primesLessThan(2000000)))
