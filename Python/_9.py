def is_pythag_triple(a, b, c):
    triplet = sorted([a, b, c])
    if (triplet[0]**2+triplet[1]**2)==(triplet[2]**2):
        return True
    return False

triplet = []
for a in range(1, 999):
    for b in range(1, 1000-(1+a)):
        c = 1000-a-b
        if is_pythag_triple(a, b, c):
            triplet = [a, b, c]
print(triplet[0]*triplet[1]*triplet[2])
