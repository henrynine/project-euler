import common, functools
'''
p = 3 * (2**(n-1)) - 1
q = 3 * (2**n) - 1
r = 9 * (2**(2*n-1)) - 1
where n > 1 is an integer and p, q, r are prime numbers, then (2**n)*p*q and (2**n)*r are amicable numbers
'''

max_num = 10000
primes = common.sieve_of_eratosthenes(max_num)

factor_sums = {n: functools.reduce(lambda x, y: x+y, common.find_all_factors(n)[:-1]) for n in range(4, max_num) if not n in primes}

amicable_numbers = []

for num in factor_sums:
    try:
        opp = factor_sums[num]
        if factor_sums[factor_sums[num]] == num and opp != num:
            if num not in amicable_numbers:
                amicable_numbers.append(num)
                amicable_numbers.append(opp)
    except KeyError:
        pass

print(sum(amicable_numbers))
