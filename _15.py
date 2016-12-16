'20 steps down, 20 steps right total'
'''
1x1: RD, DR
2x2: RRDD, RDRD, RDDR, DRRD, DRDR, DDRR
3x3: RRRDDD, RDRRDD, RDDRRD, RDDDRR, RRDRDD, RRDDRD, RRDDDR,

'''
def num_grid_paths(side_length):
    if side_length == 1:
        return 2
    '''
    mirror:
    total edge: 1
    in between: (s*(s-2)?
    recursion: ngp(s-1)
    '''
    return 2*(1 + (side_length*(side_length-2)) 2*num_grid_paths(side_length-1))
print(num_grid_paths(20))
