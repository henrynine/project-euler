def find_smallest_product(max_factor):
    if max_factor == 1:
        return 1
    else:
        previous = find_smallest_product(max_factor-1)
        candidate = previous
        while True:
            if candidate % max_factor == 0:
                return candidate
            candidate += previous

print(find_smallest_product(20))
