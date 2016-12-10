def fibonacci(n):
    if n in [0, 1]:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

total = 0
counter = 0
highest_fib = 0
while highest_fib < 4000000:
    highest_fib = fibonacci(counter)
    counter+=1
    if highest_fib%2==0:
        total+=highest_fib

print(total)
