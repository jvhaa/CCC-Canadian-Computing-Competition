import sys
input = sys.stdin.readline

def sieve_of_eratosthenes(limit):
  primes = [True] * (limit + 1)
  primes[0] = primes[1] = False
  for i in range(2, int(limit**0.5)+1):
    if primes[i]:
      for j in range(i*i, limit+1, i):
        primes[j] = False
  return {i for i in range(limit) if primes[i]}

primes = sieve_of_eratosthenes(2500000)

for i in range(int(input())):
    num = int(input())
    for p in primes:
        if 2 * num - p in primes:
            print(p, 2 *num - p)
            break
