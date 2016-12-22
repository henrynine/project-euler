with open('resources/project_euler_22.txt', 'r') as names_raw:
    names = names_raw.read().split(',')

names = [name[1:-1] for name in names]
names.sort()

score = 0

for i in range(len(names)):
    for char in names[i]:
        score += (ord(char) - ord('A') + 1) * (i+1)

print(score)
