import time, os, os.path, importlib
problems = [int(f.split('.')[0][1:]) for f in os.listdir() if f[0]=='_' and f[1]!='_']
problems.sort()
problems = ['_' + str(f) for f in problems]

start_time = time.time()
for f in problems:
    pre = time.time()
    importlib.import_module(f)
    print(f[1:]+' time: ' + str(round(time.time()-pre, 6)))
print('Total time: ' + str(round(time.time()-start_time, 6)))
