# non-uniform growing strength driven attachment of hypernetworks
import hypernetx as hnx
import random as rand
import numpy as np
import WCC2 as wc

def incident_hyperedges(H,v):
    # H: hypergraph
    # v: node
    E=list(H.incidence_dict.values())
    inc_edges=[]
    for e in E:
        if v in e:
            inc_edges.append(e)
    return inc_edges

def iterateHyperGraph(H,w,w0,lam, delta):
    # returns the next iteration of the strength attachment growing model
    # H: initial hypergraph (nodes assumed to be labelled 1,2,3...,|V|)
    # w: weights of H
    # w0: "intial weight" (model parameter)
    # lam: node arrival mean (poisson)
    # delta: updating coefficient
    weights=w.copy()
    m1=np.random.poisson(lam) #new nodes
    D=H.incidence_dict
    V=list(H.nodes)
    E=list(D.values())
    s=[wc.strength(H,w,node) for node in V]
    norm_s=[ell/sum(s) for ell in s]
    prefnodes=[]
    for i in range(0,len(V)):
        if rand.random()<norm_s[i]:
           prefnodes.append(V[i])
    for node in prefnodes:
        inc_edges=incident_hyperedges(H,node)
        for e in inc_edges:
            j=E.index(e)
            weights[j]+=delta*weights[j]/s[V.index(node)]
    weights.append(w0)
    newHyperedge=["node"+str(i) for i in range(len(V)+1,len(V)+1+len(prefnodes))]+prefnodes
    D2=D.copy()
    D2["e"+str(len(E)+1)]=newHyperedge
    return hnx.Hypergraph(D2), weights
    
def hypernetwork(m0,w0,T,lam,delta):
    # returns a hypernetwork (based on the model above) at time t
    # m0: initial number of nodes (contained within one hyperedge)
    # w0: intial weight
    # T: integer time
    # delta: updating coeff
    # lam: node arrival mean (poisson)
    D0={"e1":range(1,m0+1)}
    H=hnx.Hypergraph(D0)
    w=[w0]
    t=0
    while t<T:
        H,w=iterateHyperGraph(H,w,w0,lam,delta)
        t+=1
    return H,w

    
    
    
    
           
    
        
        
        
        
    
