import math, functools
print(functools.reduce(lambda x,y:x+y,map(int,list(str(math.factorial(100))))))
