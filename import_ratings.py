# importing ratings
import pandas as pd

ratings_data=pd.read_csv(r"C:\Users\timbo\AppData\Local\Programs\Python\Python38\Scripts\NETWORKS\ratings_data.csv")
ratingsdf=pd.DataFrame(ratings_data,columns=["movieId","rating"])
ave_ratings=dict()
ratings=ratingsdf['rating']
movieId=ratingsdf['movieId']
n=len(ratings)
for i in range(1,101):
    s=[]
    for j in range(0,n):
        if movieId[j]==i:
            s.append(ratings[j])
    if len(s)!=0:
        s=round(sum(s)/len(s),2)
        ave_ratings[str(i)]=s




    
    
        
    
        

