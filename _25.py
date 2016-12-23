import common

n = 1
f = fibonacci(n)
while len(str(f)) < 1000:
    print(n, f)
    n+=1
    f = fibonacci(n)

print(n)
