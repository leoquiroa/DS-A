import pandas as pd
from df_operations import DfOperations
class CsvProcessor:

    def __init__(self,fileops,operations) -> None:
        self.fileops = fileops
        self.operations = operations
    
    def base_file(self,one_file,date_cols):
        df = self.fileops.load_csv(one_file)
        if df.empty: return
        df = DfOperations.column_date_conversion(df,date_cols)
        self.fileops.save_parquet(df)

    def a_new_file(self,all_files,date_cols):
        for one_file in all_files:
            df_base = self.fileops.load_parquet()
            print(f"{self.fileops.run_guid} - Processing file {one_file}")
            df_current = self.fileops.load_csv(one_file)
            if df_current.empty: continue
            df_current = DfOperations.column_date_conversion(df_current,date_cols)
            self.merge_operation(df_base,df_current)
