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
        num_factors *= i

    return num_factors

def triangle_number(n):
    total = 0
    for num in range(1, n+1):
        total += num
    return total

def time_count_divisors(max_n):
    start = time.time()
    n = 1
    last_tri = triangle_number(n)
    d = count_divisors(last_tri)
    highest_c = 1
    while n < max_n:
        n += 1
        last_tri = triangle_number(n)
        d = count_divisors(last_tri)
        if d > highest_c:
            highest_c = d
    end = time.time()
    return 'highest_c: %s, time: %s' % (highest_c, end-start)


#print(last_tri)
def time_tri(n):
    start = time.time()
    tri = triangle_number(n)
    end = time.time()
    print('t = %s' % str(end-start))
