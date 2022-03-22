import numpy as np
import pandas as pd

def solution(files):
    result = []
    for a in files:
        df = pd.read_csv(a)
        # conver to date
        df['date'] = pd.to_datetime(df['date'])
        # filter by year
        obj_year = df.groupby([df.date.dt.year])
        # get date by max vol
        res_vol = df.loc[obj_year['vol'].idxmax()][['date', 'vol']]
        res_vol = res_vol.reset_index()
        # to search more than one date
        max_close = df.loc[obj_year['close'].idxmax()]['close'].tolist()
        # get dates by max close
        res_close = df.loc[df['close'].isin(max_close)][['date', 'close']]
        res_close = res_close.reset_index()
        result.append([res_vol,res_close])
    return result

if __name__ == '__main__':
    A = [
        '/home/DS-A/DataStructures/Applications/csv_files/throwsh.csv'
        ,'/home/DS-A/DataStructures/Applications/csv_files/twerche.csv'
    ] 
    solution(A)