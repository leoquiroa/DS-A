import pandas as pd

class DdlOperations:

    def __init__(self,run_guid) -> None:
        self.run_guid = run_guid

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

    def insert(self,df_base,df_insert):
        print(f"{self.run_guid} - INSERT")
        self.verify_columns(df_base,df_insert)
        print(f"{self.run_guid} - The old base df shape is {df_base.shape}")
        print(f"{self.run_guid} - The new df shape is {df_insert.shape}")
        df_base = pd.concat([df_base, df_insert], ignore_index=True)
        print(f"{self.run_guid} - The new base shape is {df_base.shape}")
        return df_base

    def update(self,df_base,df_update):
        print(f"{self.run_guid} - UPDATE")
        self.verify_columns(df_base,df_update)
        for _, row in df_update.iterrows():
            t = df_base[df_base['order_id']==row['order_id']]
            if (row['order_updated_at']>pd.to_datetime(t['order_updated_at'])).bool():
                print(f"{self.run_guid} - Update order {row['order_id']}")
                df_base = df_base.drop(t.index[0])
                df_base = pd.concat([df_base,row.to_frame().transpose()], ignore_index=True)
        return df_base

    def delete(self,df_base,df_delete):
        print(f"{self.run_guid} - DELETE")
        for _, row in df_delete.iterrows():
            t = df_base[df_base['order_id']==row['order_id']]
            if (row['order_updated_at']>pd.to_datetime(t['order_updated_at'])).bool():
                df_base = df_base.drop(t.index[0])
        return df_base
    
