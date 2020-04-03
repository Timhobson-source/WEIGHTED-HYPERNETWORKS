import hypernetx as hnx
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA
from movie_data import moviedata, movieratings
import networkx as nx
from WeightEigCentrality import *
from SubhypergraphCentrality import *
from hypergraph_projection import projection
import WCC2 as wc

D=moviedata.copy()
weights=movieratings.copy()
m=len(weights)
H=hnx.Hypergraph(D)
nodes=list(H.nodes)

########Eigenvector Centrality####################



x=Node_Eig_Centrality(H,weights)
y=Hyperedge_Eig_Centrality(H,weights)


# finding the most central nodes (actors!)
def largest(k):
    s=sorted(x,reverse=True)[0:(k+1)]
    xlist=list(x)
    central_actors={}
    for value in s:
        actors=[]
        for actor in nodes:
            i=nodes.index(actor)
            if xlist[i]==value:
                actors.append(actor)
            #if xlist[i]>value:
             #   break
        central_actors[value]=actors
    return central_actors

##########Subhypergraph Centrality################
shgC=[]
Wm=WA(H,weights)
for node in nodes:
    shgC.append( round( WC_SH(H,weights,node,W_A=Wm,k_limit=5) ,2) )
shgC=[round(e,2) for e in shgC]

# for the movie data, it is essentially too large for the unscalable metric of subhypergraph
# centrality.

##########Clustering1################

P=projection(H,weights)
c=nx.clustering(P,weight='weight')
c2=[round(v,2) for v in list(c.values())]

##########Clustering2################
wcc2list=[]
for node in nodes:
  wcc2list.append(wc.WCC2(H,weights,node))


##########Data#######################

data = {'eig. cent.':x,'subhyp cent.': shgC,'clustering1':c2,'clustering2':wcc2list}
data=pd.DataFrame(data,index=nodes, columns=['centrality','subhyp cent.','clustering'])
