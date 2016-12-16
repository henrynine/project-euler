from math import factorial as f

def combinations(n, r):
    return int(f(n) / f(r) / f(n-r))
    
print(combinations(40, 20))
