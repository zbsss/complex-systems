import numpy as np
import matplotlib.pyplot as plt

W1 = [
  [0.000, -0.500, 0.500, 0.000, 0.500, 0.000],
  [0.000, 0.500, -0.500, 0.000, 0.500, 0.500],
  [0.500, 0.000, 0.000, 0.500, 0.250, 0.500],
]

W2 = [
  [0.849, 0.037, -0.037, 0.849, 0.075, 0.1830],
  [0.197, -0.226, 0.226, 0.197, 0.400, 0.049],
  [-0.150, 0.283, 0.260, 0.237, 0.575, -0.084],
  [0.000, 0.000, 0.000, 0.160, 0.500, 0.000]
]

W3 = [
  [0.500, -0.500, 0.500, 0.21, 0.500, 0.000],
  [-0.500, 0.500, -0.500, 0.000, 0.500, 0.500],
  [-0.150, 0.283, 0.260, 0.237, 0.575, -0.084],
  [0.500, 0.21, 0.000, 0.500, 0.250, 0.500],
  [0.000, 0.000, 0.000, 0.160, 0.500, 0.000]
]

def transform(x, y, params):
  a, b, c, d, e, f = params
  return int(a * x + b * y + e), int(c * x + d * y + f)

def ifs(img, lenses, max_iters=10):
  for _ in range(max_iters):
    new_img = np.zeros((SIZE, SIZE))
    
    for i in range(SIZE):
      for j in range(SIZE):
        if img[i, j] == 1:
          for k in range(len(lenses)):
            new_img[transform(i, j, lenses[k])] = 1

    img = new_img

  return img


def ifs_random(img, lenses, max_iters=10):
  for _ in range(max_iters):
    new_img = np.zeros((SIZE, SIZE))
    
    for i in range(SIZE):
      for j in range(SIZE):
        if img[i, j] == 1:
          lens_idx, = np.random.randint(size=1,low=0, high=len(lenses))
          new_img[transform(i, j, lenses[lens_idx])] = 1

    img = new_img

  return img

SIZE = 1024
img = np.zeros((SIZE, SIZE))

img[:SIZE // 4, :] = 1
img[:, :SIZE // 4] = 1

# img = ifs(img, W3, 5)

# plt.imshow(img)
# plt.show()

img = ifs_random(img, W1, 10)

plt.imshow(img)
plt.show()
