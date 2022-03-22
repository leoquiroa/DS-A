import pandas as pd
from datetime import datetime

def solution(S):
    df_grl = get_info(S)
    df_ix = add_index_column(df_grl)
    df_ix = df_ix.assign(NewName = lambda x: x['Country']+x['IxByCountry']+x['Extension'])
    return df_ix

def get_info(S):
    df = pd.DataFrame()
    lines = S.split('\n')
    for ix,line in enumerate(lines):
        data = line.split(',')
        df2 = {
            'IxGeneral': ix
            ,'Country': data[1].strip()
            ,'Date': datetime.strptime(data[2].strip(), '%Y-%m-%d %H:%M:%S')
            ,'Extension':data[0][-4:]
        }
        df = df.append(df2, ignore_index = True)
    return df

def add_index_column(df):
    countries = list(df['Country'].unique())
    df1 = pd.DataFrame()
    for country in countries:
        df_country = df[df["Country"]==country]
        df_country = df_country.sort_values(by=['Date'])
        df_country = df_country.reset_index(drop=True)
        df_country.reset_index(inplace=True)
        df_country.rename(columns = {'index':'IxByCountry'}, inplace = True)
        df_country['IxByCountry'] = df_country['IxByCountry'].astype(str)
        df1 = df1.append(df_country, ignore_index = True)
    return df1.sort_values(by=['IxGeneral'])
        
    
if __name__ == '__main__':
    f = open("/home/DS-A/DataStructures/Applications/New Text Document.txt", "r")
    solution(f.read())