# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import numpy as np
import math

A = 2.38767
B = -1.22713
C = -0.39595
D = -4.67104

rows = 2
cols = 100

xy = np.zeros((rows, cols), dtype="f")
# xy = zeroxy.astype("f")

xy[1, 0] = 0
xy[0, 0] = 0

i = 1
while i < 100:
    xy[0, i] = math.sin(xy[1, i - 1] * A)-math.cos(xy[0,i-1] * B)
    xy[1, i] = math.sin(xy[0, i - 1] * C)-math.cos(xy[1,i-1] * D)
    #xy[0, i] = i/10
    #xy[1, i] = 2 * i/10
    print("X = " + str(xy[0, i]) + "  Y = " + str(xy[1, i]))
    print(xy[0,i])
    print(xy.dtype)
    i = i + 1





plt.plot(xy[0, :], xy[1, :])
plt.ylabel('some numbers')
plt.show()
