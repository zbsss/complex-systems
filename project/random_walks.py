
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
# import scipy.sparse.csr_matrix

def generate_ba(n, m, m0):
    """
    n - number of nodes
    m0 - number of isolated nodes at time 0,
    m - degree of new node, m <= m0
    """
    graph = nx.Graph()

    graph.add_nodes_from(range(m0))

    for j in range(m0, n):
        """
        probability of edge (j, i) is proportional to degree of node i
        """

        degrees = [deg + 1 for _, deg in graph.degree]

        total = sum(degrees)

        neighbor = np.random.choice(graph.nodes(), size=m, p=[deg / total for deg in degrees])

        for i in neighbor:
            graph.add_edge(j, i)

    return graph

graph = generate_ba(10**2, 3, 3)
A = nx.adjacency_matrix(graph).toarray()
# graph = nx.from_numpy_matrix(A)

N = len(A)

PI = np.ones((N, N))
PI /= np.sum(PI, axis=0)

i = np.random.randint(N)

heatmap = np.zeros((N, N))

alpha = 1

for t in range(100):
  """
  p(i, t) - probability that the walker occupies node i at time t

  PI[i, j]:
      - transition matrix of probabilities moving from node j to node i as time t
      - columns must sum to 1
  """
  while i == (j := np.random.choice(range(N), p=PI[i])): continue
  heatmap[i, j] += 1
  
  div = 1
  for l in range(N):
    div += A[l, j] * np.exp(alpha * np.sum(PI[l]))

  PI[i, j] = A[i, j] * np.exp(alpha * np.sum(PI[i])) / div
  
  i = j


print(heatmap)




plt.imshow(heatmap)
plt.show()
