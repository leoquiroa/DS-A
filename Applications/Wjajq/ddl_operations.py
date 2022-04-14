class DdlOperations:

    def __init__(self,fileops) -> None:
        pass
    
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