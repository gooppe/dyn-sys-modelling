import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


from itertools import product
from IPython.display import clear_output

plt.rcParams["figure.figsize"] = (10,10)

def logistic_map(x, r=4):
    return r * x * (1 - x)

size = 128
eps = 0.6
r = 4
n_iters = 40

plots = []
plot = np.random.rand(size, size)
new_plot = np.empty_like(plot)

for t in range(n_iters):
    for i in range(size):
        for j in range(size):
            top = plot[i - 1, j]
            right = plot[i, (j + 1) % size]
            bot = plot[(i + 1) % size, j]
            left = plot[i, j - 1]
            mid = plot[i, j]
            mid, *values = [logistic_map(p, r) for p in [mid, top, right, bot, left]]
            new_plot[i, j] = mid * eps + np.mean(values) * (1 - eps)
    plot = new_plot.copy()
    plots.append(plot)


fig = plt.figure()
i=0
im = plt.imshow(plots[0], animated=True)
def updatefig(*args):
    global i
    if (i<len(plots)):
        i += 1
    else:
        i=0
    im.set_array(plots[i])
    return im,
ani = animation.FuncAnimation(fig, updatefig,  blit=True)
plt.show()