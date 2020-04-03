# subhypergraph centrality
import hypernetx as hnx
import numpy as np
from math import *
from scipy import sparse

def WA(H,w):
    # H: hypernetwork (hnx)
    # w: list of weights
    V=list(H.nodes)
    E=[list(e) for e in list(H.incidence_dict.values())]
    rowlist=[]
    for i in V:
        row=[]
        for j in V:
            val=0
            for e in E:
                if i in e and j in e:
                    val+=w[E.index(e)]
            row.append(val)
        rowlist.append(row)
    return np.array(rowlist)

def w_mu(H,w,k,i,W_A):
    # H: hypergraph (hnx)
    # w: weight list
    # k: walk length
    # i: node
    # WA: weight adj matrix
    V=list(H.nodes)
    W=sparse.csr_matrix(W_A)
    d,U=sparse.linalg.eigs(W,k=1,return_eigenvectors=True)
    dk=np.array([lam**k for lam in list(d)])
    U2=np.array([u**2 for u in list(U[V.index(i),:])])
    return np.dot(U2,dk)

def WC_SH(H,w,i,W_A,k_limit=10):
    # H: hypergraph
    # w: weight list
    # i: node
    s=0
    for k in range(0,k_limit):
        s+=w_mu(H,w,k,i,W_A)/factorial(k)
    return s
    
    
    
    
    
