# eigenvector centrality of weighted hypernetworks
import hypernetx as hnx
import numpy as np

def Wmatrix(H,w):
    # returns numpy array of weight matrix of H
    # H: hypergraph (hnx)
    # w: weight list of H
    D=H.incidence_dict
    E=[list(e) for e in list(D.values())]
    V=list(H.nodes)
    matlist=[]
    for i in V:
        row=[]
        for j in E:
            if i in j:
                row.append(w[E.index(j)])
            else:
                row.append(0)
        matlist=matlist+[row]
    return np.array(matlist)
                
def Node_Eig_Centrality(H,w):
    W=Wmatrix(H,w)
    K=np.dot(W,W.T)
    u,v=np.linalg.eigh(K)
    return abs(v[:,-1])

def Hyperedge_Eig_Centrality(H,w):
    W=Wmatrix(H,w)
    K=np.dot(W.T,W)
    u,v=np.linalg.eigh(K)
    return abs(v[:,-1])
