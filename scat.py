import numpy as np
import matplotlib.pyplot as plt


x = [0,0,0,0,7,4,9,5,8,9,9,9,0,0,0,0,14,5,8,5,13,6,7,6,5]
y = [6,8,7,9,11,11,0,11,7,9,6,7,7,6,7,0,0,7,6,6,8,7,6,10,6]
cols = ['b','g']
plt.scatter(x, y,c=cols, alpha=0.5)
plt.savefig("scatter")
