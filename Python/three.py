def find_smallest_factor(num):
    for potential_factor in range(2, int(num/2)+1):
        if num%potential_factor==0:
            return potential_factor
    return num

def find_prime_factors(num):
    factors = []
    factor = find_smallest_factor(num)
    while num != factor:#while num isn't prime
        factors.append(factor)
        num /= factor
        factor = find_smallest_factor(num)
    factors.append(int(factor))
    return factors

print(find_prime_factors(600851475143)[-1])
