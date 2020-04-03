#!/usr/bin/env python
# coding: utf-8

# In[113]:


import hypernetx as hnx
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import pandas as pd
import random as rand
import cmath
from sklearn.linear_model import LinearRegression
from math import *

from movie_data import moviedata, movieratings
import WeightEigCentrality as wec
import SubhypergraphCentrality as shc
import ERweightedmodels as er
import WCC2 as wc
import WeightedPreferredAttachment as wpa
from hypergraph_projection import projection


# In[46]:


# We define a rv U~Unif(0,5). So U-ER(n,m,p) can have weights between 0-5.
def UER(n,m,p):
    # returns weighted hypergraph~ER model with weights~unif(0,5).
    # n: number of vertices
    # m: number of hyperedges
    # p: node-hyperedge incidence probability
    D=dict()
    weights=[]
    for egde in range(0,m):
        edge_elements=[]
        for node in range(0,n):
            r=rand.random()
            if r<p:
                edge_elements.append(node+1)
        u=round(5*rand.random(),3)
        weights.append(u)
        D[str(u)]=edge_elements
    return hnx.Hypergraph(D), weights

# chung-Lu so we can get U-CL(d,k) with U~unif(0.5)
def UCL(d,k):
    # returns a hypergraph sampled from Chung-Lu configuration model
    # d: vertex degree sequence (list)
    # k: hyperedge dimension/order sequence (list)
    n=len(d) #number of vertices
    m=len(k) #number of hyperedges
    c=sum(d)
    weights=[]
    l=max([u*v for u in d for v in k])
    if c!=sum(k) or l>=c:
        return "error: degree and dimension sequences invalid"
    else:
        D=dict()
        for edge in range(0,m):
            weights.append(5*rand.random())
            edgelist=[]
            for node in range(0,n):
                r=rand.random()
                if r<d[node]*d[edge]/c:
                    edgelist.append(node+1)
            D[str(edge+1)]=edgelist
    return hnx.Hypergraph(D), weights

def degrees(H):
    return [len(list(H.neighbors(node))) for node in list(H.nodes)]

def ave_WCC1(hgraph,weights):
    P=projection(hgraph,weights)
    wcc1=nx.clustering(P,weight='weight').values()
    return sum(wcc1)/len(wcc1)

def ave_WCC2(hgraph,weights):
    wcc2=[wc.WCC2(hgraph,weights,node) for node in list(hgraph.nodes)]
    return sum(wcc2)/len(wcc2)

def getcomps(H):
    comps=H.s_components
    counter=0
    for comp in comps:
        counter+=1
    return counter


# In[3]:


# UER modelling moviedata:
def UERmodel():
    n=1448
    m=47
    average_hyperedge_size=32.212765957446805
    p_star=average_hyperedge_size/n
    G1,w1=UER(n,m,p_star)
    
    # calculating number of components ##########
    comps=G1.s_components(s=1)
    counter=0
    for comp in comps:
        counter+=1
    #print('number of 1-connnected components:',counter)

    # calculating average hyperstrength
    ave_stren=wc.ave_strength(G1,w1)
    #print("Ave hyperstrength:", )

    # Clustering1 (WCC1)
    # might also take a bit of time computationally
    G1_CC1=ave_WCC1(G1,w1)
    #print('ave WCC1 clustering:',G1_CC1)

    # Clustering (WCC2)
    G1_CC2=ave_WCC2(G1,w1)
    #print('ave WCC2 clustering:',G1_CC2)
    return [counter,ave_stren,G1_CC1,G1_CC2]

vals=[0,0,0,0]
for i in range(0,5):
    q=UERmodel()
    for j in range(0,3):
        vals[j]+=q[j]
print(vals)


# In[23]:


# U-Chung-Lu modelling of movie data

#import movie data first
Mweights=movieratings.copy()
Mhypergraph=hnx.Hypergraph(moviedata)
d=degrees(Mhypergraph)
k=[len(hyperedge) for hyperedge in moviedata.values()]
c1=sum(d)
c2=sum(k)
print(c1,c2)
# unable to be modelled by UCLmodel 


# In[20]:


# UER modelling moviedata:
def UCLmodel():
    G1,w1=UCL(d,k)
    
    # calculating number of components
    comps=G1.s_components(s=1)
    counter=0
    for comp in comps:
        counter+=1
    #print('number of 1-connnected components:',counter)

    # calculating average hyperstrength
    ave_stren=wc.ave_strength(G2,w2)
    #print("Ave hyperstrength:", )

    # Clustering1 (WCC1)
    # might also take a bit of time computationally
    G2_CC1=ave_WCC1(G2,w2)
    #print('ave WCC1 clustering:',G1_CC1)

    # Clustering (WCC2)
    G2_CC2=ave_WCC2(G2,w2)
    #print('ave WCC2 clustering:',G1_CC2)
    return [counter,ave_stren,G2_CC1,G2_CC2]

print(UCLmodel())
#vals=[0,0,0,0]
#for i in range(0,5):
 #   q=UCLmodel()
  #  for j in range(0,3):
   #     vals[j]+=q[j]
#print(vals)


# In[47]:


n=1448
m=47
t=47
m0=32
lam=(n-m0)/t
w0=1.5
delta=0.141
slist=[]
complist=[]

for j in range(0,5):
    G3,w3=wpa.hypernetwork(m0,w0,t,lam,delta)
    slist.append(wc.ave_strength(G3,w3)complist.append(getcomps(G3))
print(comlist,slist)


# In[138]:


n=1448
m=47
t=46
m0=32
lam=(n-m0)/t
w0=1.5
delta=0.141
flist=[]
for i in range(0,5):
    G3,w3=wpa.hypernetwork(m0,w0,t,lam,delta)
    comps=G3.s_components(s=1)
    counter=0
    for comp in comps:
        counter+=1
    #print('number of 1-connnected components:',counter)

    # calculating average hyperstrength
    ave_stren=wc.ave_strength(G3,w3)
    #print("Ave hyperstrength:", )

    # Clustering1 (WCC1)
    # might also take a bit of time computationally
    G3_CC1=ave_WCC1(G3,w3)
    #print('ave WCC1 clustering:',G1_CC1)

    # Clustering (WCC2)
    G3_CC2=ave_WCC2(G3,w3)
    f=[ave_stren,G3_CC1,G3_CC2,counter,len(list(G3.nodes)),len(list(G3.edges))]
    flist.append(f)

for i in range(0,6):
    total=0
    for ff in flist:
        total+=ff[i]
    print(total/10)


# In[ ]:





# In[ ]:




