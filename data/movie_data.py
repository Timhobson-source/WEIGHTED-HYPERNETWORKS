# creating weights
import pandas as pd

# we get the average ratings data (copy & pasted from results of print(ave_ratings) in import_ratings.py:

ave_ratings={'1': 3.87, '2': 3.4, '3': 3.16, '4': 2.38, '5': 3.27, '6': 3.88, '7': 3.28, '8': 3.8, '9': 3.15, '10': 3.45, '11': 3.69, '12': 2.86,
             '13': 3.94, '14': 3.45, '15': 2.32, '16': 3.95, '17': 3.92, '18': 3.29, '19': 2.6, '20': 2.54, '21': 3.54, '22': 3.36, '23': 3.09,
             '24': 3.04, '25': 3.74, '26': 4.1, '27': 3.14, '28': 4.08, '29': 4.03, '30': 4.05, '31': 3.18, '32': 3.92, '34': 3.6, '35': 3.55, '36': 3.94,
             '37': 2.0, '38': 2.0, '39': 3.55, '40': 3.92, '41': 4.02, '42': 2.33, '43': 3.62, '44': 2.7, '45': 3.52, '46': 3.17, '47': 4.03, '48': 2.93,
             '49': 4.0, '50': 4.37, '52': 3.64, '53': 5.0, '54': 3.67, '55': 3.33, '57': 3.14, '58': 4.0, '59': 4.0, '60': 2.83, '61': 3.57, '62': 3.69,
             '63': 2.83, '64': 2.4, '65': 2.02, '66': 2.0, '68': 3.5, '69': 3.82, '70': 3.02, '71': 2.43, '72': 3.17, '73': 4.12, '74': 3.03, '76': 3.33,
             '77': 4.0, '78': 3.2, '79': 2.96, '80': 4.62, '81': 3.25, '82': 3.8, '83': 3.0, '84': 4.0, '85': 4.06, '86': 3.76, '87': 1.67, '88': 2.89,
             '89': 3.44,'92': 3.54, '93': 2.23, '94': 3.57, '95': 3.18, '96': 1.0, '97': 3.88, '98': 3.0, '99': 2.75, '100': 3.43}


# we have node/hyperedge data:

credits_df = pd.read_csv(r"C:\Users\timbo\AppData\Local\Programs\Python\Python38\Scripts\NETWORKS\credits_data.csv")
creds=pd.DataFrame(credits_df, columns=["id","cast"])
creds=creds.astype({'id':"str"})

castlists=creds['cast']
Ids=creds['id']   
movies=dict()
movie_number=0
for movie in castlists:
    exec("D="+movie)
    castlist=[]
    for actor in D:
        name=actor['name']
        castlist.append(name)
    movies[Ids[movie_number]]=castlist
    movie_number+=1

moviedata={}
movieratings=[]
for i in range(0,100):
    j=str(i)
    if j in ave_ratings.keys():
        if j in movies.keys():
            moviedata[j]=movies[j]
            movieratings.append(ave_ratings[j])

            
            
