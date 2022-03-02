import pandas


class ImportData:

    def read_csv(self, filepath):
        print(f'Loading JSON from {filepath}')
        dataframe = pandas.read_csv(filepath)
        return dataframe
