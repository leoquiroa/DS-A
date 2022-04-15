import pandas as pd

class DdlOperations:

    def __init__(self,run_guid) -> None:
        self.run_guid = run_guid

    def insert(self,df_base,df_insert):
        print(f"{self.run_guid} - INSERT")
        print(f"{self.run_guid} - The old base df shape is {df_base.shape}")
        print(f"{self.run_guid} - The new df shape is {df_insert.shape}")
        df_base = pd.concat([df_base, df_insert], ignore_index=True)
        print(f"{self.run_guid} - The new base shape is {df_base.shape}")
        return df_base

    def update(self,df_base,df_update):
        print(f"{self.run_guid} - UPDATE")
        for _, row in df_update.iterrows():
            t = df_base[df_base['order_id']==row['order_id']]
            if (row['order_updated_at']>pd.to_datetime(t['order_updated_at'])).bool():
                print(f"{self.run_guid} - Update order {row['order_id']} succesfully")
                df_base = df_base.drop(t.index[0])
                df_base = pd.concat([df_base,row.to_frame().transpose()], ignore_index=True)
            else:
                print(f"{self.run_guid} - The order {row['order_id']} was not updated")
        return df_base

    def delete(self,df_base,df_delete):
        print(f"{self.run_guid} - DELETE")
        for _, row in df_delete.iterrows():
            t = df_base[df_base['order_id']==row['order_id']]
            df_base.loc[t.index[0], "is_order_deleted"] = True
            print(f"{self.run_guid} - The order {row['order_id']} was marked as deleted")
        return df_base
    
