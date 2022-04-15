import uuid
from file_operations import FileOperations
from df_operations import DfOperations

class CsvProcessor:

    def __init__(self,folder_input,folder_output,final_file) -> None:
        self.run_guid = uuid.uuid4()
        print(f"{self.run_guid} - Begin process")
        self.fileops = FileOperations(folder_input,folder_output,final_file,self.run_guid)
        self.dfops = DfOperations(self.run_guid)
    
    def base_file(self,one_file,date_col):
        df = self.fileops.load_csv(one_file)
        if df.empty: 
            print(f"{self.run_guid} - The file {one_file} is empty ")
            return
        df = self.dfops.date_conversion(df,date_col)
        self.fileops.save_parquet(df)

    def subsequent_files(self,all_files,date_col):
        for one_file in all_files:
            df_base = self.fileops.load_parquet()
            print(f"{self.run_guid} - The base file has {len(df_base)} rows")
            df_current = self.fileops.load_csv(one_file)
            print(f"{self.run_guid} - Processing {len(df_current)} rows from file {one_file}")
            if df_current.empty: 
                print(f"{self.run_guid} - The file {one_file} is empty ")
                continue
            df_current = self.dfops.date_conversion(df_current,date_col)
            df_base = self.dfops.merge(df_base,df_current)
            self.fileops.save_parquet(df_base)
            print(f"{self.run_guid} - The base file has {len(df_base)} rows")
        print(f"{self.run_guid} - End process")
