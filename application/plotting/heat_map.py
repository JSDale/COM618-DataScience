from import_data import ImportData
import seaborn as sns
import os
import time


class HeathMapPlotting:

    def plot(self, filepath):
        data_frame = ImportData.read_json(filepath)
        try:
            df_heatmap = data_frame.pivot('Date', 'Death_by_Location')
            plot = sns.heatmap(df_heatmap, annot=True)
            fig = plot.figure
            fig.savefig(f'{os.getcwd()}\\..\\graphs\\heatmap_{time.time()}.png')
            print(f'saved at: {filepath}')
        except Exception as e:
            print(str(e))
            raise
