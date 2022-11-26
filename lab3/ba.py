import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


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

# params = [(3, 10**2), (3, 10**3), (2, 10**5), (3, 10**5)]
params = [(3, 10**2)]

for m, n in params:
    graph = generate_ba(n, m, m)

    print(graph)
    nx.draw_kamada_kawai(graph)
    plt.savefig(f"{n=}_{m=}.png")
