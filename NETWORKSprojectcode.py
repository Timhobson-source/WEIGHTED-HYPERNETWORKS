#!/usr/bin/env python
# coding: utf-8

# In[14]:


# imports
import WCC2 as wc
import hypernetx as hnx
import matplotlib.pyplot as plt
from movie_data import moviedata, movieratings
from math import *
import networkx as nx
import WeightEigCentrality as wec
import SubhypergraphCentrality as shc
import ERweightedmodels as er
import WeightedPreferredAttachment as wpa
from hypergraph_projection import projection
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import cmath


# In[40]:


D=moviedata.copy()
weights=movieratings.copy()
MoviesHypergraph=hnx.Hypergraph(D)
nodes=list(MoviesHypergraph.nodes)
print('number of nodes:',len(nodes))
print('Number of hyperedges:',len(MoviesHypergraph.edges))
L=[len(e) for e in D.values()]
print('Average hyperedge size:',sum(L)/len(L))
print(sum(weights)/len(weights))


# In[3]:


hnx.draw(MoviesHypergraph,with_node_labels=False, with_edge_labels=False) # or with H.collapse_nodes()
plt.show()


# In[16]:


# eigenvector centrality.
x=wec.Node_Eig_Centrality(MoviesHypergraph,weights) #node eig centrality
y=wec.Hyperedge_Eig_Centrality(MoviesHypergraph,weights) #hyperedge eig centrality
def largest(k,cent):
    s=sorted(cent,reverse=True)[0:(k+1)]
    xlist=list(cent)
    central_actors={}
    for value in s:
        actors=[]
        for actor in nodes:
            i=nodes.index(actor)
            if xlist[i]==value:
                actors.append(actor)
        central_actors[round(value,3)]=actors
    return central_actors
print(largest(20,cent=x)) #shows most central actor is Harrison Ford (more or less as expected)


# In[18]:


# subhypergraph centrality
# computationally this takes a lot of time
subhypgraphC=[]
Wm=shc.WA(MoviesHypergraph,weights)
for node in nodes:
    subhypgraphC.append( round( shc.WC_SH(MoviesHypergraph,weights,node,W_A=Wm,k_limit=5) ,2) )
subhypgraphC=[round(e.real,2) for e in subhypgraphC]
print(largest(20,cent=subhypgraphC))


# In[19]:


cent1=x
cent2=subhypgraphC

X = np.array([[c] for c in cent1])
y = np.array(cent2)
reg = LinearRegression().fit(X, y)
predict=reg.predict(X)

plt.scatter(cent1,cent2,c="r")
plt.plot(X,predict,c="b")
plt.legend(['lm fit','centralities'])
plt.xlabel('Eigenvector Centrality')
plt.ylabel('Subhypergraph Centrality')
plt.show()
print('r^2 score:',reg.score(X, y))
# pretty correlation r^2 very close to 1. It is worth noting that both centralities in this graph show a small
# number of nodes with high centrality and the majority of nodes with virtually none. 
# This is representative because: (see report).


# In[20]:


# Clustering1 (CC1)
# might also take a bit of time computationally
P=projection(MoviesHypergraph,weights)
cc1=nx.clustering(P,weight='weight')
cc1=[round(v,2) for v in list(cc1.values())]


# In[21]:


# Clustering2 (CC2)

from cc2data import cc2data
#cc2=cc2data
cc2=[]
# code used to produce cc2data:
for node in nodes:
   cc2.append(wc.WCC2(MoviesHypergraph,weights,node))
# It just takes a while computationally, didn't want to do it again.


# In[24]:


print("global cc1:",sum(cc1)/len(cc1))
print("gloabl cc2:",sum(cc2)/len(cc2))
print("Ave hyperstrength:", wc.ave_strength(MoviesHypergraph,weights))
X = np.array([[c] for c in cc1])
y = np.array(cc2)
reg = LinearRegression().fit(X, y)
predict=reg.predict(X)

plt.scatter(cc1,cc2,c='r')
plt.plot(X,predict,c='b')
plt.legend(['lm fit','clustering coeffs.'])
plt.xlabel('CC1')
plt.ylabel('CC2')
plt.show()
print("r^2 score:", reg.score(X,y)) # almost no correlation between the two clustering coefficients in this data

comps=MoviesHypergraph.s_components(s=1)
counter=0
for comp in comps:
    counter+=1
print("Movie hypergraph 1-connected components:",counter)


# In[ ]:





# In[69]:


# generative/configuration models
# ER models
N=100
ratio=0.7
p=0.7
G1cc1=[]
G1cc2=[]
G2cc1=[]
G2cc2=[]
for n in range(4,N+4):
    m=floor(ratio*n)
    G1=er.unifER(n,m,p)
    w1=[float(e) for e in G1.edges]
    #G2=er.unifdegER(n,m,p)
    #w2=[float(e) for e in G2.edges]
    P1=projection(G1,w1)
    #P2=projection(G2,w2)
    G1cc1.append(sum(list(nx.clustering(P1,weight='weight').values()))/len(P1.nodes))
    #G2cc1.append(sum(list(nx.clustering(P2,weight='weight').values()))/len(P2.nodes))
    G1cc2.append(wc.aveWCC2(G1,w1))
    #G2cc2.append(wc.aveWCC2(G2,w2))
Ns=range(1,N+1)
plt.plot(Ns,G1cc1,'bs')
plt.plot(Ns,G1cc2,'rs')
plt.legend(['WCC1','WCC2'])
plt.xlabel('Number of Nodes')
plt.ylabel('Clustering coefficients of U-ER model: p='+str(p))
#plt.plot(Ns,G2cc1,'g^',G2cc2,'y^')
plt.show()
    
    


# In[6]:


uniflist=[]
unifdeglist=[]
for node in list(G1.nodes):
    uniflist.append(wc.WCC2(G1,w1,node))
for node in list(G2.nodes):
    unifdeglist.append(wc.WCC2(G2,w2,node))
m1=sum(uniflist)/len(uniflist)
m2=sum(unifdeglist)/len(unifdeglist)
print("G1 global WCC2 is:",m1)
print("G2 global WCC2 is:",m2)

plt.scatter(list(G1.nodes),uniflist,c="r")
plt.axhline(m1,c="r")
plt.scatter(list(G2.nodes),unifdeglist,c="b")
plt.axhline(m2,color="b")
plt.show()


# In[ ]:


S1=[]
S2=[]
for node in list(G1.nodes):
    S1.append(wc.strength(G1,w1,node))
for node in list(G2.nodes):
    S2.append(wc.strength(G2,w2,node))


# In[47]:


T=47
n=1
m0=32
w0=1.5
lam=(1448-m0)/T
delta=0.6

ave_hypstrength=[]
    total=0
    for d in [0.3*f for f in range(1,11)]:
        H,w=wpa.hypernetwork(m0,w0,T,lam,d)
        total+=wc.ave_strength(H,w)
    total=total/n
    ave_hypstrength.append(total)
time=range(1,T+1)

logtime=[log(u) for u in time]

X = np.array([[c] for c in logtime])
y = np.array(ave_hypstrength)
reg = LinearRegression().fit(X, y)
predict=reg.predict(X)
print('r^2 score:',reg.score(X,y) )
plt.scatter(time,ave_hypstrength,c="r")
plt.axhline(4.397,c="b")
#plt.plot(X,predict,c="b")
plt.xlabel("time")
plt.ylabel("average hyperstrength")

plt.show()

X2=np.array([[c] for c in ave_hypstrength])
y2=np.array(logtime)
re2=LinearRegression().fit(X2, y2)
#t_star=reg.predict(np.array([4.397]),y2)
#print(t_star)


# In[90]:


from statsmodels.distributions.empirical_distribution import ECDF
mhs=[]
for node in nodes:
    mhs.append(wc.strength(MoviesHypergraph,weights,node))

m0=2
w0=2
lam=1
#delta=1
t=5

def gen_hs(m0,w0,t,lam,delta):
    hs=[]
    H,w=wpa.hypernetwork(m0,w0,t,lam,delta)
    for node in list(H.nodes):
        hs.append(wc.strength(H,w,node))
    return hs
legend=[] 
ds=[0.5,1,2,4,6]
for d in ds:
    emp=ECDF(gen_hs(m0,w0,t,lam,d))
    plt.plot(emp.x,emp.y)
    legend+=['delta='+str(d)]
movie_emp=ECDF(mhs)
plt.plot(movie_emp.x,movie_emp.y,c="black")
plt.xlabel('hyperstrength')
plt.ylabel('cdf')
legend=legend+['movies']
plt.legend(legend)
plt.show()


# In[92]:


from statsmodels.distributions.empirical_distribution import ECDF
mhs=[]
for node in nodes:
    mhs.append(wc.strength(MoviesHypergraph,weights,node))

m0=2
#w0=2
lam=1
delta=1
t=5

legend=[] 
#lams=[1,3,5,7]
#ms=[1,2,4,6]
ws=[1,2,4,6]
#ds=[0.5,1,2,4,6]
for w in ws:
    emp=ECDF(gen_hs(m0,w,t,lam,d))
    plt.plot(emp.x,emp.y)
    legend+=['w='+str(w)]
movie_emp=ECDF(mhs)
plt.plot(movie_emp.x,movie_emp.y,c="black")
plt.xlabel('hyperstrength')
plt.ylabel('cdf')
legend=legend+['movies']
plt.legend(legend)
plt.show()


# In[95]:


from statsmodels.distributions.empirical_distribution import ECDF
mhs=[]
for node in nodes:
    mhs.append(wc.strength(MoviesHypergraph,weights,node))

m0=2
w0=2
#lam=1
delta=1
t=5

legend=[] 
lams=[1,3,5,7]
#ms=[1,2,4,6]
for lam in lams:
    emp=ECDF(gen_hs(m0,w0,t,lam,d))
    plt.plot(emp.x,emp.y)
    legend+=['lam='+str(lam)]
movie_emp=ECDF(mhs)
plt.plot(movie_emp.x,movie_emp.y,c="black")
plt.xlabel('hyperstrength')
plt.ylabel('cdf')
legend=legend+['movies']
plt.legend(legend)
plt.show()


# In[96]:


from statsmodels.distributions.empirical_distribution import ECDF
mhs=[]
for node in nodes:
    mhs.append(wc.strength(MoviesHypergraph,weights,node))

#m0=2
w0=2
lam=1
delta=1
t=5

legend=[] 
#lams=[1,3,5,7]
ms=[1,2,4,6]
for m in ms:
    emp=ECDF(gen_hs(m,w0,t,lam,d))
    plt.plot(emp.x,emp.y)
    legend+=['m0='+str(m)]
movie_emp=ECDF(mhs)
plt.plot(movie_emp.x,movie_emp.y,c="black")
plt.xlabel('hyperstrength')
plt.ylabel('cdf')
legend=legend+['movies']
plt.legend(legend)
plt.show()


# In[ ]:




