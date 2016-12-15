def next_collatz(n):
    if n % 2 == 0:
        return int(n/2)
    return 3*n + 1

def count_collatz_steps(n):
    steps = 0
    while n != 1:
        steps += 1
        n = next_collatz(n)
    return steps

most_steps = (0, 0)
for n in range(1, 1000000):
    steps = count_collatz_steps(n)
    if steps > most_steps[1]:
        most_steps = (n, steps)
print(most_steps[0])
