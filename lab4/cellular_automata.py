import numpy as np
import matplotlib.pyplot as plt
import math 

n = 100
max_ones = 50
iterations = 100
window = 3

image = np.full((iterations, n), 0)

ones_idx = np.random.choice(range(n), size=max_ones, replace=False)
image[0, ones_idx] = 1

window_map = {
  (1, 1, 1): 1,
  (1, 1, 0): 0,
  (1, 0, 1): 1,
  (1, 0, 0): 1,
  (0, 1, 1): 1,
  (0, 1, 0): 0,
  (0, 0, 1): 0,
  (0, 0, 0): 0,
}

for i in range(1, iterations):
  image[i] = image[i - 1]
  for mid in range(0, n):
    image[i, mid] = window_map[tuple(image[i - 1, [mid-1, mid, mid + 1 if mid + 1 < n else 0]])]

plt.imshow(image)
plt.show()
