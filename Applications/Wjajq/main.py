import os
from pathlib import Path
import pandas as pd
import numpy as np
import uuid

class FileOps:

    def __init__(self,folder_input,folder_output,final_file) -> None:
        root = Path(__file__).parent
        self.data_input = f"{root}/{folder_input}"
        self.data_output = f"{root}/{folder_output}"
        self.final_file = f"{self.data_output}/{final_file}"
        self.run_guid = uuid.uuid4()

    def check_folders(self):
        if not os.path.exists(self.data_output): 
            os.makedirs(self.data_output)
        if not os.path.exists(self.data_input): 
            os.makedirs(self.data_input)

    def load_csv(self,one_file):
        print(f"{self.run_guid} - Reading {one_file}")
        file_path = f"{self.data_input}/{one_file}"
        if not os.path.exists(file_path): 
            print(f"{self.run_guid} - File {file_path} does not exist")
            return
        return pd.read_csv(f"{self.data_input}/{one_file}")

    def save_parquet(self,df):
        df.to_parquet(self.final_file, compression='gzip', engine='pyarrow')
        print(f"{self.run_guid} - Saving {self.final_file}")

    def load_parquet(self):
        if not os.path.exists(self.final_file): 
            print(f"{self.run_guid} - File {self.final_file} does not exist")
            return
        print(f"{self.run_guid} - Loading {self.final_file}")
        return pd.read_parquet(self.final_file)

class Processor:

    def __init__(self,fileops,operations) -> None:
        self.fileops = fileops
        self.operations = operations
    
    def base(self,one_file,date_cols):
        df = self.fileops.load_csv(one_file)
        if df.empty: return
        df = self.column_date_conversion(df,date_cols)
        self.fileops.save_parquet(df)

    def a_new_file(self,all_files,date_cols):
        for one_file in all_files:
            df_base = self.fileops.load_parquet()
            print(f"{self.fileops.run_guid} - Processing file {one_file}")
            df_current = self.fileops.load_csv(one_file)
            if df_current.empty: continue
            df_current = self.column_date_conversion(df_current,date_cols)
            self.merge_operation(df_base,df_current)

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

    def merge_operation(self,df_base,df_current):
        list_intersect = self.get_intesection(df_base, df_current)
        df_update, df_delete = self.is_in_operation(df_current,list_intersect)
        df_insert = self.is_not_in_operation(df_current,list_intersect)

        # 1. INSERT
        self.verify_columns(df_base,df_insert)
        df_base = pd.concat([df_base, df_op_i])
        print(f"{self.fileops.run_guid} - The newcomer rows shape is {df_op_i.shape}")
        print(f"{self.fileops.run_guid} - The new base shape is {new_base.shape}")
        # 2. UPDATE
        for _, row in df_op_u.iterrows():
            t = new_base[new_base['order_id']==row['order_id']]
            if (row['order_updated_at']>pd.to_datetime(t['order_updated_at'])).bool():
                new_base = new_base.drop(t.index[0])
                new_base = new_base.concat(row, ignore_index=True)
        # 3. DELETE
        for _, row in df_op_d.iterrows():
            t = new_base[new_base['order_id']==row['order_id']]
            if (row['order_updated_at']>pd.to_datetime(t['order_updated_at'])).bool():
                new_base = new_base.drop(t.index[0])
                new_base.append(row, ignore_index=True)
        # Change the base 
        self.fileops.save_parquet(new_base)

    def column_date_conversion(self,df,cols):
        # change column type to date time
        for col in cols:
            if col in df.columns: 
                df[col] =  pd.to_datetime(df[col])
        return df

if __name__ == '__main__':
    # input parameters
    all_files = [
        'Homework task @ Initial Data.csv'
        ,'Homework task @ CDC 2021-06-17.csv'
        ,'Homework task @ CDC 2021-06-18.csv'
        ,'Homework task @ CDC 2021-06-19.csv'
    ]
    folder_input = "input_data"
    folder_output = "output_data"
    final_file = "df.parquet.gzip"
    operations = ['INSERT','UPDATE','DELETE']
    date_cols = ['order_updated_at']
    # file operations
    fileops = FileOps(folder_input,folder_output,final_file)
    fileops.check_folders()
    processor = Processor(fileops,operations)
    processor.base(all_files[0],date_cols)
    processor.a_new_file(all_files[1:],date_cols)

