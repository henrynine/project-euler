from _18 import get_highest_path
triangle = []
with open('resources/euler_67_triangle.txt', 'r') as t:
    raw = t.read()
    stripped = raw.replace(' 0', ' ')#no need for twice because no 00
    rows = stripped.split('\n')[:-1]#get rid of null char at end
    for row in rows:
        triangle.append(row.split(' '))
print(get_highest_path(triangle, 0, 0)[0])
