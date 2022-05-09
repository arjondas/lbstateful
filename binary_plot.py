import numpy as np
from matplotlib.pyplot import step, show, plot


data = [  [1, 0, 0, 1, 1, 0, 1, 0],
          [1, 0, 1, 1, 0, 1, 0, 0],
          [1, 1, 0, 1, 0, 1, 1, 1] ]
count = 0
for x in data:
    step(np.arange(0,len(x),1), [ _x + count for _x in x])
    count += 2

show()
