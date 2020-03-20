import numpy as np
x = np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y = np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
x_sum = np.sum(x)
y_sum = np.sum(y)
x1 = x_sum/x.size
y1 = y_sum/y.size
i = 0
up = 0
down = 0
while i<x.size:
    up += ((x[i]-x1)*(y[i]-y1))
    down += ((x[i]-x1)*(x[i]-x1))
    i+=1
w = up/down
b = y1-(w*x1)
print("w = ",w," b = ",b)