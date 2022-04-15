import pandas as pd

class DfOperations:

    def __init__(self,fileops) -> None:
        self.fileops = fileops

    def column_date_conversion(self,df,cols):
        for col in cols:
            if col in df.columns: 
                df[col] =  pd.to_datetime(df[col])
        return df

    def get_intesection(self,df_base, df_current):
        df_intersect = pd.merge(df_base, df_current, on=['order_id'], how='inner')
        return list(df_intersect['order_id'])

    def is_in_operation(self,df_current,list_intersect):
        df_op = df_current[df_current['order_id'].isin(list_intersect)]
        df_update = df_op[df_op['operation'] == 'UPDATE']
        df_delete = df_op[df_op['operation'] == 'DELETE']
        df_check = df_op[df_op['operation'] == 'INSERT']
        if len(df_check) > 0:
            order_id_list = ','.join([str(x) for x in df_check['order_id']])
            print(f"{self.fileops.run_guid} - Warning, illegal operation for order {order_id_list}")
        if len(df_update) > 0:
            print(f"{self.fileops.run_guid} - {len(df_update)} rows are going to be updated")
        if len(df_delete) > 0:
            print(f"{self.fileops.run_guid} - {len(df_delete)} rows are going to be deleted")
        del df_update['operation']
        del df_delete['operation']
        return df_update, df_delete

    def is_not_in_operation(self,df_current,list_intersect):
        df_op = df_current[~df_current['order_id'].isin(list_intersect)]
        df_insert = df_op[df_op['operation'] == 'INSERT']
        df_check = df_op[df_op['operation'] != 'INSERT']
        if len(df_check) > 0:
            order_id_list = ','.join([str(x) for x in df_check['order_id']])
            print(f"{self.fileops.run_guid} - Warning, illegal operation for order {order_id_list}")
        if len(df_insert) > 0:
            print(f"{self.fileops.run_guid} - {len(df_insert)} rows are going to be inserted")
        del df_insert['operation']
        return df_insert

    def verify_columns(self,df_base,df_insert):
        a = set(df_base.columns)
        b = set(df_insert.columns)
        existing = a.difference(b)
        new_columns = b.difference(a)
        matches = a.intersection(b)
        print(f"{self.fileops.run_guid} - The matching columns are {len(matches)} and they are {matches}")
        print(f"{self.fileops.run_guid} - The already existing columns are {len(existing)} and they are {existing}")
        print(f"{self.fileops.run_guid} - The new columns are {len(new_columns)} and they are {new_columns}")
