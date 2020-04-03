# testing of clustering coefficients for weighted generatove models

from ERweightedmodels import unifER, unifdegER
from hypergraphs1 import cc, AVEcc

N=10
n=15
m=10
p=0.5
unifAVEcclist=[]
unifdegAVEcclist=[]
for i in range(0,N):
    H1=unifER(n,m,p)
    H2=unifdegER(n,m,p)
    unifAVEcclist.append(AVEcc(H1))
    unifdegAVEcclist.append(AVEcc(H2))

mean_unif=sum(unifAVEcclist)/len(unifAVEcclist)
mean_degunif=sum(unifdegAVEcclist)/len(unifdegAVEcclist)
print("unif mean:", mean_unif)
print("unif deg mean:", mean_degunif)


