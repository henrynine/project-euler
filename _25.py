import common

n = 1
f = common.fibonacci(n)
while len(str(f)) < 1000:
    print(n, f)
    n+=1
    f = common.fibonacci(n)

print(n)
