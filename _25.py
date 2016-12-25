import common, decimal

decimal.getcontext().prec = 1100
dec = decimal.Decimal

n = dec(1)
f = common.big_fibonacci(n)

while len(str(f)) < 1000:
    n+=1
    f = common.big_fibonacci(n)

print(n)
