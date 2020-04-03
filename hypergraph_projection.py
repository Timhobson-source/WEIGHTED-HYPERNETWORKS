# hypergraph to graph projection 
import hypernetx as hnx
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def projection(H,w):
    # H: hypergraph (assumed weighted)
    # w: hyperedge weights
    weights=w.copy()
    nodes=list(H.nodes)
    E=list(H.incidence_dict.values())
    E=[list(e) for e in E]
    m=len(weights)
    n=len(nodes)
    rowlist=[]
    for node1 in nodes:
        row=[]
        for node2 in nodes:
            val=0
            for edge in E:
                if node1 in edge:
                    if node2 in edge:
                        if nodes.index(node1)!=nodes.index(node2):
                            val+=weights[E.index(edge)]
            row.append(val)
        rowlist.append(row)
    A=np.array(rowlist)
    return nx.Graph(A)
