import math, time, operator, functools

def find_smallest_factor(num):#assists find_prime_factors
    for potential_factor in range(2, int(num/2)+1):
        if num%potential_factor==0:
            return potential_factor
    return num

def find_factors(num):
    l = list(set(functools.reduce(operator.add,
              ([n, num//n] for n in range(1, int(math.sqrt(num)) + 1) if num%n==0))))
    l.sort()
    return l

def find_prime_factors(num):
    factors = []
    factor = find_smallest_factor(num)
    while num != factor:#while num isn't prime
        factors.append(factor)
        num /= factor
        factor = find_smallest_factor(num)
    factors.append(int(factor))
    return factors

def get_binaries(l):#assists find_all_factors
    base = lambda n: bin(n)[2:]
    return ['0' * (l-len(base(n))) + base(n) for n in range(1, 2**l)]

def find_all_factors(num):
    prime_factors = find_prime_factors(num)
    all_factors = [1]
    for bin_code in get_binaries(len(prime_factors)):
        factor = 1
        for i in range(len(bin_code)):
            if int(bin_code[i]):
                factor *= prime_factors[i]
        all_factors.append(factor)
    all_factors = list(set(all_factors))
    all_factors.sort()
    return all_factors

def sieve_of_eratosthenes(max_num):
    primes = []
    candidates = {n: True for n in range(2, max_num)}
    for p in range(2, max_num):
        if candidates[p]:
            primes.append(p)
            for n in range(p, max_num, p):
                candidates[n] = False
    return primes

def sieve_of_sundaram(max_num):
    new_max = int(max_num/2)
    primes = []
    candidates = {n: True for n in range(1, new_max)}
    for i in range(1, new_max):
        for j in range(i, new_max):
            t = i+j+2*i*j
            if t > new_max:
                break
            if t in candidates and t < new_max:
                candidates[t] = False
        if i**2 > new_max:
            break
    primes = [2]
    for n in candidates:
        if candidates[n] == True:
            primes.append(n*2+1)
    return primes

def prime_wheel(starting_primes, max_num):#currently doesn't work
    perimeter = 1
    for prime in starting_primes:
        perimeter *= prime
    base_circle = [n for n in range(2, perimeter+1)]#remainder of one does not disqualify, so start at two
    candidates = [n for n in range(2, max_num)]
    base_primes = base_circle
    for prime in starting_primes:
        for base_circle_num in range(prime, perimeter+1, prime):
            if base_circle_num in base_primes and base_circle_num not in starting_primes:
                base_primes.remove(base_circle_num)
    potential_primes = [n for n in candidates]
    for candidate in candidates:
        remainder = candidate % perimeter
        if (remainder not in base_primes and remainder != 1) or (remainder in starting_primes):
            potential_primes.remove(candidate)
    return potential_primes

def is_prime(num):#instant for 2^31-1
    for n in range(2, int(math.sqrt(num))):
        if num % n == 0:
            return False
    return True

def brute_prime_filter(candidates):
    primes = []
    for candidate in candidates:
        if is_prime(candidate):
            primes.append(candidate)
    return primes
