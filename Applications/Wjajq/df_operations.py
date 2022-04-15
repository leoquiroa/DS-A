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
        list_intersect = self.get_intesection(df_base, df_current)
        df_update, df_delete = self.is_in(df_current,list_intersect)
        df_insert = self.is_not_in(df_current,list_intersect)
        df_base = self.ddloperations.insert(df_base,df_insert)
        df_base = self.ddloperations.update(df_base,df_update)
        df_base = self.ddloperations.delete(df_base,df_delete)
        return df_base

    def get_intesection(self,df_base, df_current):
        df_intersect = pd.merge(df_base, df_current, on=['order_id'], how='inner')
        return list(df_intersect['order_id'])

    def is_in(self,df_current,list_intersect):
        df_op = df_current[df_current['order_id'].isin(list_intersect)]
        df_update = df_op[df_op['operation'] == 'UPDATE']
        df_delete = df_op[df_op['operation'] == 'DELETE']
        df_check = df_op[df_op['operation'] == 'INSERT']
        if len(df_check) > 0:
            order_id_list = ','.join([str(x) for x in df_check['order_id']])
            print(f"{self.run_guid} - Warning, illegal operation for order {order_id_list}")
        if len(df_update) > 0:
            print(f"{self.run_guid} - {len(df_update)} rows are going to be updated")
        if len(df_delete) > 0:
            print(f"{self.run_guid} - {len(df_delete)} rows are going to be deleted")
        del df_update['operation']
        del df_delete['operation']
        return df_update, df_delete

    def is_not_in(self,df_current,list_intersect):
        df_op = df_current[~df_current['order_id'].isin(list_intersect)]
        df_insert = df_op[df_op['operation'] == 'INSERT']
        df_check = df_op[df_op['operation'] != 'INSERT']
        if len(df_check) > 0:
            order_id_list = ','.join([str(x) for x in df_check['order_id']])
            print(f"{self.run_guid} - Warning, illegal operation for order {order_id_list}")
        if len(df_insert) > 0:
            print(f"{self.run_guid} - {len(df_insert)} rows are going to be inserted")
        del df_insert['operation']
        return df_insert

    
