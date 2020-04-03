import hypernetx as hnx
import matplotlib.pyplot as plt
import s_connected as scn
from movie_data import moviedata, movieratings

def noborder(width=10,height=10):
    fig = plt.figure(figsize=[width,height])
    ax = plt.gca()
    ax.axis('off')

weights=movieratings
hyperedges=moviedata

m=len(weights)
incidence_dict=dict()
for i in range(0,m):
    incidence_dict[str(weights[i])]=hyperedges[list(hyperedges.keys())[i]]

H=hnx.Hypergraph(moviedata)#incidence_dict)
nodes=list(H.nodes)
print(len(H.edges))
hyperdegrees=[]
for node in nodes:
    hyperdegrees.append(H.degree(node))

def f(L,n):
    # returns the indexs of the largest n values in L
    # L: list type
    # n: integer type
    Lsorted=sorted(L,reverse=True)[0:n]
    indexes=[]
    for value in Lsorted:
        indexes.append(L.index(value))
    return indexes
# doesnt work. :( 
imp_nodes=[nodes[i] for i in f(hyperdegrees,100)] # 100 nodes with highest hyperdegrees
dict2=dict()
for edge in incidence_dict:
    t=False
    for node in imp_nodes:
        if node in incidence_dict[edge]:
            t=True
    if t==True:
        dict2[edge]=incidence_dict[edge]
H2=hnx.Hypergraph(dict2)

#noborder()
#hnx.draw(H2, with_node_labels=False, with_edge_labels=True)
#plt.show()

