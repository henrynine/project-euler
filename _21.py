import common, functools
'''
p = 3 * (2**(n-1)) - 1
q = 3 * (2**n) - 1
r = 9 * (2**(2*n-1)) - 1
where n > 1 is an integer and p, q, r are prime numbers, then (2**n)*p*q and (2**n)*r are amicable numbers
'''

max_num = 100
primes = common.sieve_of_eratosthenes(max_num)


for n in range(2, max_num):
    print(common.find_prime_factors(n)[:-1])

factor_sums = {n: functools.reduce(lambda x, y: x+y, common.find_prime_factors(n)[:-1]) for n in range(4, max_num) if not n in primes}
backwards_fs = {v: k for k, v in factor_sums.items()}
print('fs: ' + str(factor_sums))
print('bfs: ' +  str(backwards_fs))

amicable_numbers = []

for num in factor_sums:
    pass

total = 0
for pair in find_amicable_numbers_max(max_num):
    total += sum(pair)

print(total)
