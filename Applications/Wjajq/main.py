from file_operations import FileOperations
from csv_processor import CsvProcessor

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
    fileops = FileOperations(folder_input,folder_output,final_file)
    fileops.check_folders()
    processor = CsvProcessor(fileops,operations)
    processor.base_file(all_files[0],date_cols)
    processor.a_new_file(all_files[1:],date_cols)

