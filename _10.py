from common import sieve_of_eratosthenes
total = 0
for prime in sieve_of_eratosthenes(2000000):
    total += prime
print(total)
