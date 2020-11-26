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

n = 100000

xy = np.zeros((2, n), dtype="f")

i = 1
while i < n:
    xy[0, i] = math.sin(xy[1, i - 1] * A)-math.cos(xy[0,i-1] * B)
    xy[1, i] = math.sin(xy[0, i - 1] * C)-math.cos(xy[1,i-1] * D)
    #print("X = " + str(xy[0, i]) + "  Y = " + str(xy[1, i]))
    i += 1


plt.scatter(xy[0, :], xy[1, :], 0.0001, c='black')
plt.axis('off')
plt.show()
