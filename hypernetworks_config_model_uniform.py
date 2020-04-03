import hypernetx as hnx
import random as rand
#import matplotlib.pyplot as plt
from math import *
#from hypergraphs1 import cc, AVEcc

def ER_config_model(n,m,p):
    # returns a hypergraph sampled from the ER configuration model
    # n: number of nodes
    # m: number of hyperedges
    # p: probability of node being in a hyperedge
    D=dict()
    for edge in range(1,m+1):
        edgeset=[]
        for node in range(1,n+1):
            r=rand.random()
            if r<p:
                edgeset.append(node)
        D[str(edge)]=edgeset
    return hnx.Hypergraph(D)


                
