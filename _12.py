import time, math
from common import find_prime_factors

def count_divisors(n):
    if n == 1:
        return 1

    prime_factors = find_prime_factors(n)
    prime_factors_no_repeats = []

    for prime in prime_factors:
        if prime not in prime_factors_no_repeats:
            prime_factors_no_repeats.append(prime)
    factor_counts = {n: 0 for n in prime_factors_no_repeats}

    for prime in prime_factors:
        factor_counts[prime] += 1

    num_factors = 1
    for i in factor_counts.values():
        num_factors *= (i+1)

    return num_factors

def triangle_number(n):
    return(sum(range(n)))

most_divisors = (1, 1)
n = 1
while most_divisors[1] < 500:
    last_tri = triangle_number(n)
    n += 1
    d = count_divisors(last_tri)
    if d > most_divisors[1]:
        most_divisors = (last_tri, d)
print(most_divisors[0])
