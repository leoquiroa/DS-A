import pandas as pd
from ddl_operations import DdlOperations

class DfOperations:

    def __init__(self,run_guid) -> None:
        self.run_guid = run_guid
        self.ddloperations = DdlOperations(self.run_guid)

    def date_conversion(self,df,col):
        if col in df.columns: 
            df[col] =  pd.to_datetime(df[col])
        return df

    def merge(self,df_base,df_current):
        df_insert = df_current[df_current['operation'] == 'INSERT']
        del df_insert['operation']
        self.verify_columns(df_base,df_insert)
        df_insert = self.remove_repetions(df_insert)
        print(f"{self.run_guid} - {len(df_insert)} rows are going to be inserted")
        df_base = self.ddloperations.insert(df_base,df_insert)
        df_update = df_current[df_current['operation'] == 'UPDATE']
        del df_update['operation']
        print(f"{self.run_guid} - {len(df_update)} rows are going to be updated")
        df_base = self.ddloperations.update(df_base,df_update)
        df_delete = df_current[df_current['operation'] == 'DELETE']
        del df_delete['operation']
        print(f"{self.run_guid} - {len(df_delete)} rows are going to be deleted")
        df_base = self.ddloperations.delete(df_base,df_delete)
        return df_base

    def verify_columns(self,df_base,df_insert):
        a = set(df_base.columns)
        b = set(df_insert.columns)
        matches = a.intersection(b)
        old_columns = a.difference(b)
        new_columns = b.difference(a)
        if len(matches) > 0:
            print(f"{self.run_guid} - The matching columns are {len(matches)}")
        if len(old_columns) > 0:
            print(f"{self.run_guid} - The columns that are not in the new df are {len(old_columns)} : {old_columns}")
        if len(new_columns) > 0:
            print(f"{self.run_guid} - The new columns from the new df are {len(new_columns)} : {new_columns}")

    def remove_repetions(self,df_insert):
        df_count = df_insert.groupby(['order_id'])['order_id'].size().reset_index(name='counts')
        if len(df_count[df_count['counts']>1])==0: return df_insert
        repetitions = list(df_count[df_count['counts']>1]['order_id'])
        for element in repetitions:
            filtered = df_insert[df_insert['order_id']==element]['order_updated_at']
            del_ix = [x for x in list(filtered.index) if x != filtered.idxmax()]
            print(f"{self.run_guid} - Remove repeated order {element}")
            df_insert.drop(del_ix, axis=0, inplace=True)
        return df_insert

    
