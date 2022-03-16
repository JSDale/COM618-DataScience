import pandas


class ImportData:

    def read_csv(self, filepath):
        print(f'Loading CSV from {filepath}')
        dataframe = pandas.read_csv(filepath)
        return dataframe

    @staticmethod
    def read_json(filepath):
        print(f'Loading JSON from {filepath}')
        data_frame = pandas.read_json(filepath)
        return data_frame
