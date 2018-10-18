# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 14:40:52 2018

@author: Administrator
"""

import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
G = nx.Graph()
G.add_node("v1")
G.add_node("v2")
G.add_node("v3")
G.add_node("v4")
G.add_node("v5")
G.add_node("v6")
G.add_node("v7")
G.add_node("v8")

G.add_edge("v1" , "v2")
G.add_edge("v1" , "v5")
G.add_edge("v1" , "v7")
G.add_edge("v1" , "v8")
G.add_edge("v2" , "v8")
G.add_edge("v3" , "v4")
G.add_edge("v5" , "v6")
G.add_edge("v5" , "v7")
G.add_edge("v5" , "v8")
G.add_edge("v7" , "v8")

nx.draw(G, with_label =True)
plt.show()
print(nx.is_connected(G))
#print(list(nx.dfs_preorder_nodes(G,'v1')))
print(list(nx.dfs_preorder_nodes(G,)))