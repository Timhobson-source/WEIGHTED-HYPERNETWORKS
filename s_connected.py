# s-connected graph

import hypernetx as hnx

def s_connected_component(H,s):
    # H: hypergraph (hnx format)
    # s: parameter for hyperedge restriction
    D=H.incidence_dict
    newD=dict()
    for edge in D:
        if len(D[edge])>=s:
            newD[edge]=D[edge]
    return hnx.Hypergraph(newD)


    
            
                        
    
    
