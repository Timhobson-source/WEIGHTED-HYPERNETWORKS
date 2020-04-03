import pandas as pd

credits_df = pd.read_csv(r"C:\Users\timbo\AppData\Local\Programs\Python\Python38\Scripts\NETWORKS\credits_data.csv")
creds=pd.DataFrame(credits_df, columns=["id","cast"])
cast=creds['cast']
Ids = creds['id']
names=[]
movies=dict()
movie_number=0
for movie in cast:
    exec("D="+movie)
    castlist=[]
    count=0
    for actor in D:
        name=actor['name']
        castlist.append(name)
        count+=1
    movies[movie_number]=castlist
    names+=castlist
    movie_number+=1
names = list(dict.fromkeys(names))

    
