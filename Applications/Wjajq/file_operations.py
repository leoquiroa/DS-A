from pathlib import Path
import pandas as pd
import uuid
import os

class FileOperations:

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
