import pandas as pd

class DdlOperations:

    def __init__(self,run_guid) -> None:
        self.run_guid = run_guid

    def verify_columns(self,df_base,df_insert):
        a = set(df_base.columns)
        b = set(df_insert.columns)
        existing = a.difference(b)
        new_columns = b.difference(a)
        matches = a.intersection(b)
        print(f"{self.run_guid} - The matching columns are {len(matches)} and they are {matches}")
        print(f"{self.run_guid} - The already existing columns are {len(existing)} and they are {existing}")
        print(f"{self.run_guid} - The new columns are {len(new_columns)} and they are {new_columns}")

    def insert(self,df_base,df_insert):
        self.verify_columns(df_base,df_insert)
        df_base = pd.concat([df_base, df_insert])
        print(f"{self.run_guid} - The newcomer df shape is {df_insert.shape}")
        print(f"{self.run_guid} - The new base shape is {df_base.shape}")
        return df_base

    def update(self,df_base,df_update):
        self.verify_columns(df_base,df_update)
        for _, row in df_update.iterrows():
            t = df_base[df_base['order_id']==row['order_id']]
            if (row['order_updated_at']>pd.to_datetime(t['order_updated_at'])).bool():
                df_base = df_base.drop(t.index[0])
                df_base = df_base.concat(row, ignore_index=True)
        return df_base

    def delete(self,df_base,df_delete):
        for _, row in df_delete.iterrows():
            t = df_base[df_base['order_id']==row['order_id']]
            if (row['order_updated_at']>pd.to_datetime(t['order_updated_at'])).bool():
                df_base = df_base.drop(t.index[0])
        return df_base
    
