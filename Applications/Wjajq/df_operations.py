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
        df_insert = self.filter_df(df_current,'INSERT')
        self.verify_columns(df_base,df_insert)
        df_insert = self.remove_repetions(df_insert)
        print(f"{self.run_guid} - {len(df_insert)} rows are going to be inserted")
        df_base = self.ddloperations.insert(df_base,df_insert)
        df_update = self.filter_df(df_current,'UPDATE')
        print(f"{self.run_guid} - {len(df_update)} rows are going to be updated")
        df_base = self.ddloperations.update(df_base,df_update)
        df_delete = self.filter_df(df_current,'DELETE')
        print(f"{self.run_guid} - {len(df_delete)} rows are going to be deleted")
        df_base = self.ddloperations.delete(df_base,df_delete)
        return df_base

    def filter_df(self,df_current,operation):
        df_operation = df_current[df_current['operation'] == operation]
        del df_operation['operation']
        return df_operation

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
        df_local = df_insert.copy()
        df_count = df_local.groupby(['order_id'])['order_id'].size().reset_index(name='counts')
        if len(df_count[df_count['counts']>1])==0: return df_local
        repetitions = list(df_count[df_count['counts']>1]['order_id'])
        for element in repetitions:
            filtered = df_local[df_local['order_id']==element]['order_updated_at']
            del_ix = [x for x in list(filtered.index) if x != filtered.idxmax()]
            print(f"{self.run_guid} - Remove repeated order {element}")
            df_local.drop(del_ix, axis=0, inplace=True)
        return df_local

    
