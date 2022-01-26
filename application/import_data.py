import os
import pandas


class ImportData:
    
    def convert_csv_to_json(self, filepath):
        print("hello world.")
        data_frame = pandas.read_csv(filepath)
        filepath = filepath.replace('.csv', '.json')
        print(f'saving to: {filepath}')
        data_frame.to_json(filepath)
        print(f'saved to: {filepath}')
        