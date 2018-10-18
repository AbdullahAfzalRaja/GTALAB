# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 14:40:52 2018

@author: Administrator
"""

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph([(0, 0), (0, 1), (0, 2), (1, 2), (2, 0), (2, 1), (2, 2)])
nx.draw(G, with_labels=True)
plt.show()
print(len(list(nx.simple_cycles(G))))

copyG = G.copy()
copyG.remove_nodes_from([1])
copyG.remove_edges_from([(0, 1)])

print(len(list(nx.simple_cycles(copyG))))
