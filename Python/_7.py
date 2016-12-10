def sieve_of_eratosthenes(max_num):
    candidates = [n for n in range(3, max_num+1)]
    primes = [2]
    while primes[-1] != candidates[-1]:
        for n in candidates:
            if n%primes[-1] == 0:
                candidates.remove(n)
        primes.append(candidates[0])
    return primes

print(sieve_of_eratosthenes(150000)[10000])
