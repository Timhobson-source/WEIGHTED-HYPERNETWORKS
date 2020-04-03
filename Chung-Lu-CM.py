# Chung-Lu configuration model
import hypernetx as hnx
import random as rand
#from math import *
#import matplotlib.pyplot as plt

def CL(d,k):
    # returns a hypergraph sampled from Chung-Lu configuration model
    # d: vertex degree sequence (list)
    # k: hyperedge dimension/order sequence (list)
    n=len(d) #number of vertices
    m=len(k) #number of edges
    c=sum(d)
    l=max([u*v for u in d for v in k])
    if c!=sum(k) or l>=c:
        return "error: degree and dimension sequences invalid"
    else:
        D=dict()
        for edge in range(0,m):
            edgelist=[]
            for node in range(0,n):
                r=rand.random()
                if r<d[node]*d[edge]/c:
                    edgelist.append(node+1)
            D[str(edge+1)]=edgelist
        return hnx.Hypergraph(D)

