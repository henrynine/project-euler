'''
make all permutations
sort
get millionth
'''
import common, functools, operator

def permutations(n):
    permutation_list = []
    this_digit = str(n-1)
    if n == 1:
        return ['0']
    #insert n-1 digit into each spot of permuation below
    for p in permutations(n-1):
        for i in range(n):
            #insert at i
            permutation_list.append(p[:i] + this_digit + p[i:])
    return permutation_list

p = permutations(10)
p.sort()
print(p[999999])
