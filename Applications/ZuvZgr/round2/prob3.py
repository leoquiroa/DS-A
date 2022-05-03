import pandas as pd

def solution():
    root = '/home/DS-A/Applications/TopTal/data3'
    users = pd.read_csv(f'{root}/users.csv',delimiter=r"|")
    movies = pd.read_csv(f'{root}/movies.csv',delimiter=r"|")
    ratings = pd.read_csv(f'{root}/ratings.csv',delimiter=r"|")
    print('-')

    name = 'Ryan James'
    year = 1995

    user_id = int(users[users['full name']==name]['user id'])
    seen = ratings[ratings['user id']==user_id]
    z = seen[['item id','rating']]


    user_id = int(users[users['full name']==name]['user id'])
    not_seen = ratings[ratings['user id']!=user_id]
    gb = not_seen.groupby(by=['item id'])['item id'].count().reset_index(name="count")
    gb.rename(columns = {'item id':'movie id'}, inplace = True)
    mrg = pd.merge(gb,movies,on="movie id",)
    year_filter = mrg[mrg['release year']==year]
    sorted = year_filter.sort_values(by=['count','movie title'],ascending=False)
    sorted.iloc[0]['movie title']

    user_id = int(users[users['full name']==name]['user id'])
    not_seen = ratings[ratings['user id']!=user_id]
    gb = not_seen.groupby('item id')['rating'].mean().reset_index(name="count")
    gb.rename(columns = {'item id':'movie id'}, inplace = True)
    mrg = pd.merge(gb,movies,on="movie id",)
    year_filter = mrg[mrg['release year']==year]
    sorted = year_filter.sort_values(by=['count','movie title'],ascending=False)
    sorted.iloc[0]['movie title']


    #result = [x for x in lines if 'NULL' not in x]
    

if __name__ == '__main__':
    R = []
    R.append("id,name,age,score\n1,Jack,NULL,12\n17,Betty,28,11") 
    # "id,name,age,score\n17,Betty,28,11
    R.append("header,header\nANNUL,ANNULLED\nnull,NILL\nNULL,NULL") 
    # "header,header\nANNUL,ANNULLED\nnull,NILL"
    R.append("country,population,area\nUK,67m,242000km2") 
    # "country,population,area\nUK,67m,242000km2"
    #for r in R:
        #print(r,solution(r))
    solution()
        

    