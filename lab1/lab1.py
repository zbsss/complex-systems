import numpy as np
import imageio
from collections import defaultdict
import matplotlib.pyplot as plt

L = 100
MAX_HEIGHT = 4
MAX_ITERATIONS = 30000
ITERATIONS_PER_FRAME = 100
FILENAME = 'mygif.gif'

grid = np.zeros((L, L))
# grid = np.random.choice((range(MAX)), size=(L, L))


def add_grain_bfs(i, j, visited):
    if (i not in range(L) or
        j not in range(L) or
            (i, j) in visited):
        return

    grid[i, j] += 1
    visited.add((i, j))

    if grid[i, j] == MAX_HEIGHT:
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            add_grain_bfs(i + di, j + dj, visited)
        grid[i, j] = 0


avalanches_count = defaultdict(lambda: 0)
images = []
for t in range(MAX_ITERATIONS):
    if t % ITERATIONS_PER_FRAME == 0:
        images.append(grid.copy())

    i, j = np.random.randint(low=0, high=L, size=2)

    visited = set()
    add_grain_bfs(i, j, visited)

    if visited:
        avalanches_count[len(visited)] += 1

x = np.array([int(size) for size in avalanches_count.keys()])
y = np.array([int(size) for size in avalanches_count.values()])

print(x)

xlog = np.log(x)
ylog = np.log(y)

plt.scatter(xlog, ylog)

# fig = plt.figure()
# ax = plt.gca()
# ax.plot(avalanches_count.keys(), avalanches_count.values(), 'o', c='blue', markeredgecolor='none')
# ax.set_yscale('log')
# ax.set_xscale('log')
plt.show()

# build GIF
# with imageio.get_writer(FILENAME, mode='I') as writer:
#     for image in images:
#         writer.append_data(image)
