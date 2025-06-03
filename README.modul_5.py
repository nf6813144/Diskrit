# Modul 5
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_edges_from ([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'A')])

plt.figure(figsize = (6, 4))
nx.draw(G, with_labels = True, node_color = 'purple', edge_color = 'brown', node_size = 850)
plt.title("Representasi Graf")
plt.show()

print("Adjacency List:")
for node in G.adj:
  print(f"{node}: {list(G.adj [node])}")
