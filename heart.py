import os
import numpy as np
from time import sleep

rows, columns = os.popen('stty size', 'r').read().split()
columns = int(columns) - 53

print(rows, columns)
print("\033[31m")
# print("\033[101m") 
def heart(itp = 0):
    # size 53 * 23
    resx = -0.05
    resy = -0.1
    s = -1.3
    for y in np.arange(-s, s, resy):
        print(" " * itp, end = "")
        for x in np.arange(-s, s, resx):
            if((y**2 + x**2 - 1)**3 <= (x**2)*(y**3)):
                print('#', end = '')
            else :
                print(' ', end = '')
        sleep(0.1)
        print()
    print(" " * 35, ".")

try:
    while(1):
        heart(np.random.randint(columns))
except KeyboardInterrupt:
        print("\033[00m")
