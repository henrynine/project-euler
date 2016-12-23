import common, time, functools, operator

abundants = [n for n in range(1, 28123-12+1) if sum(common.find_factors(n)[:-1]) > n]
total = 0

abundant_sums = set()

for n in abundants:
    for m in abundants:
        if n+m > 28123:
            break
        abundant_sums.add(n+m)

non_sums = set(range(1, 28124)).difference(abundant_sums)

print(functools.reduce(operator.add, non_sums))
