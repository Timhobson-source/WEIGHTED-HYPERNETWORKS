# Clustering2 WCC_2
import hypernetx as hnx

def strength(H,w,k):
    # returns the (hyper)strength of a node in a weighted hypergraph
    # H: hypergraph
    # w: weights of hypergraph
    # k: node in H
    E=[list(e) for e in H.incidence_dict.values()]
    total=0
    for e in E:
        if k in e:
            total+=w[E.index(e)]
    return total

def ave_strength(H,w):
    total=0
    V=list(H.nodes)
    for k in V:
        total+=strength(H,w,k)
    return total/len(V)

def WCC2(H,w,v):
    E=[list(e) for e in H.incidence_dict.values()]
    V=list(H.nodes)
    strengthlist=[]
    for node in V:
        strengthlist.append(strength(H,w,node))
    m=max(strengthlist)
    s_hat=[e/m for e in strengthlist]
    m=max(strengthlist)
    total=0
    N1=set(H.neighbors(v))
    for u in V:
        N2=set(H.neighbors(u))
        I=N1.intersection(N2)
        for k in I:
            total+=s_hat[V.index(k)]/len(I)
    return total/len(V)

def aveWCC2(H,w):
    total=0
    for node in list(H.nodes):
        total+=WCC2(H,w,node)
    return total/len(list(H.nodes))
    
