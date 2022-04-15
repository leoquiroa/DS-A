#from file_operations import FileOperations
from csv_processor import CsvProcessor

if __name__ == '__main__':
    initial_file = 'Homework task @ Initial Data.csv'
    other_files = [
        'Homework task @ CDC 2021-06-17.csv'
        ,'Homework task @ CDC 2021-06-18.csv'
        ,'Homework task @ CDC 2021-06-19.csv'
    ]
    folder_input = "input_data"
    folder_output = "output_data"
    final_file = "df.parquet.gzip"
    date_col = 'order_updated_at'
    processor = CsvProcessor(folder_input,folder_output,final_file)
    processor.base_file(initial_file,date_col)
    processor.subsequent_files(other_files,date_col)

