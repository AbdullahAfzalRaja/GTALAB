# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import networkx as nx
import matplotlib.pyplot as plt
G = nx.DiGraph()
G.add_node("142")
G.add_node("143")
G.add_node("378")
G.add_node("370")
G.add_node("341")
G.add_node("321")
G.add_node("326")
G.add_node("322")
G.add_node("421")
G.add_node("401")

G.add_edge("142" , "143")
G.add_edge("143" , "321")
G.add_edge("143" , "341")
G.add_edge("143" , "370")
G.add_edge("143" , "378")
G.add_edge("321" , "322")
G.add_edge("321" , "326")
G.add_edge("322" , "421")
G.add_edge("322" , "401")
G.add_edge("326" , "421")
G.add_edge("326" , "401")
G.add_edge("341" , "401")
G.add_edge("378" , "401")

nx.draw(G, with_labels =True)
plt.show()
#print(nx.is_connected(G))
print("DFS Transversal")
dfs = list(nx.dfs_edges(G))
print(dfs)
dfs_node = list(nx.dfs_preorder_nodes(G))
print("DFS Node")
print(dfs_node)

print("Topological Order")
topolological = list(nx.topological_sort(G))
print(topolological)

#print(list(nx.topological_sort(nx.line_graph(G))))