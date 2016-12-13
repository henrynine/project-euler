def sum_squares(max_num):
    total = 0
    for n in range(1, max_num+1):
        total += n**2
    return total

def squared_sum(max_num):
    to_square = 0
    for n in range(1, max_num+1):
        to_square += n
    return to_square**2

print(squared_sum(100)-sum_squares(100))
