from pathlib import Path
import pandas as pd
import os

class FileOperations:

    def __init__(self,folder_input,folder_output,final_file,run_guid) -> None:
        root = Path(__file__).parent
        self.folder_input = f"{root}/{folder_input}"
        self.folder_output = f"{root}/{folder_output}"
        self.final_file = f"{self.folder_output}/{final_file}"
        self.run_guid = run_guid

    def load_csv(self,one_file):
        print(f"{self.run_guid} - Reading csv {one_file}")
        file_path = f"{self.folder_input}/{one_file}"
        if not os.path.exists(file_path): 
            print(f"{self.run_guid} - File {file_path} does not exist")
            return
        return pd.read_csv(f"{self.folder_input}/{one_file}")

    def save_parquet(self,df):
        self.check_output_folder()
        df.to_parquet(self.final_file, compression='gzip', engine='pyarrow')
        print(f"{self.run_guid} - Saving parquet {self.final_file}")

    def check_output_folder(self):
        if not os.path.exists(self.folder_output): 
            os.makedirs(self.folder_output)

    def load_parquet(self):
        if not os.path.exists(self.final_file): 
            print(f"{self.run_guid} - File {self.final_file} does not exist")
            return
        print(f"{self.run_guid} - Loading parquet {self.final_file}")
        return pd.read_parquet(self.final_file)
