# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:42:39 2018

@author: Administrator
"""

import networkx as nx
import matplotlib.pyplot as plt
G= nx.DiGraph()
G.add_node("00")
G.add_node("01")
G.add_node("10")
G.add_node("11")
G.add_node("20")
G.add_node("21")
G.add_edge("00","01")
G.add_edge("01","10")
G.add_edge("10","11")
G.add_edge("11","00")
G.add_edge("11","20")
G.add_edge("20","21")
nx.draw(G, with_labels=True)
plt.show()
print(len(list(nx.simple_cycles(G))))

copyG = G.copy()
copyG.remove_edges_from([("10", "11")])
print(len(list(nx.simple_cycles(copyG))))
nx.draw(copyG, with_labels=True)
plt.show()