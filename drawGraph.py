
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import networkx as nx

import requests

response = requests.get('https://drawgraph.herokuapp.com/?fbclid=IwAR17_cUzGZjnBaFnLbCXOGL3lX6xcrCXhyLwd4fT4zxzU9IZxPjDqqjtezM')
resData = response.json()

G = nx.DiGraph()

G.add_edge(str(resData[0]['importedFile']), str(resData[3]['importedFile']), weight=0)
G.add_edge(str(resData[3]['importedFile']), str(resData[2]['importedFile']), weight=0)
G.add_edge(str(resData[4]['importedFile']), str(resData[2]['importedFile']), weight=1)
G.add_edge(str(resData[1]['importedFile']), str(resData[4]['importedFile']), weight=1)

#

zero = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 0]
one = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 1]
# two = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 2]
# three = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] == 3]

pos = nx.spring_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=300)

# edges
nx.draw_networkx_edges(G, pos, edgelist=zero,
                       width=6, edge_color='g', arrowsize=30, arrowstyle='fancy')
nx.draw_networkx_edges(G, pos, edgelist=one,
                       width=6, edge_color='y', arrowsize=30, arrowstyle='fancy')
# nx.draw_networkx_edges(G, pos, edgelist=two,
#                        width=6, edge_color='y', arrowsize=30, arrowstyle='fancy')
# nx.draw_networkx_edges(G, pos, edgelist=three,
#                        width=6, edge_color='y', arrowsize=30, arrowstyle='fancy')

# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

plt.axis('off')
plt.show()

