#go left is +0, go right is +1
sample = [[3],
          [7, 4,],
          [2, 4, 6],
          [8, 5, 9, 3]]

triangle = [[75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

cache = {}
'''
find choice below with highest path itself, then take that
so work up from second to bottom row then back down
'''
c = 0
def get_highest_path(triangle, row, right):#returns [value, [path]]
<<<<<<< HEAD
    global c, cache
    if (row, right) in cache:
        return cache[(row, right)]
    c += 1
    print(row, right)
=======
>>>>>>> parent of 39f39d3... start 67
    value = triangle[row][right]
    if row == len(triangle) - 1:#bottom row
        cache[(row, right)] = value
        return [value, []]#[value, [no path]
    else:
        left_path = get_highest_path(triangle, row+1, right)
        right_path = get_highest_path(triangle, row+1, right+1)
        if left_path[0] > right_path[0]:#left value is greater
            cache[(row, right)] = value + left_path[0]
            return [value + left_path[0], [0] + left_path[1]]#return value of self and path with left step at this row
        else:#right value is greater
            cache[(row, right)] = value + right_path[0]
            return [value + right_path[0], [1] + right_path[1]]#return value of self and path with right step at this row
print(get_highest_path(triangle, 0, 0)[0])
print('c: ' + str(c))
