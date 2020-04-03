#!/usr/bin/env python
# coding: utf-8
import hypernetx as hnx

def cc(node1,node2,H):
    # returns the clustering coefficient of two nodes in a hypergraph
    # H: hypergraph
    N1=set(H.neighbors(node1))
    N2=set(H.neighbors(node2))
    a=len(N1.intersection(N2))
    b=len(N1.union(N2))
    return a/b

def AVEcc(H):
    # returns average clusteringcoefficient of a hypergraph
    s=0
    nodes=list(H.nodes)
    n=len(nodes)
    for i in range(0,n):
        for j in range(i+1,n):
            s+=cc(nodes[i],nodes[j],H)
    num_node_pairs=n*(n-1)*0.5
    return s/num_node_pairs
    

