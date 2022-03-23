import datetime
import matplotlib.pyplot as plt


class LineGraphPlotting:

    def plot(self, df_arr, save_path):
        figure = plt.figure()
        for i in range(len(df_arr)):
            df = df_arr[i]
            del df['new_deaths_with_positive_test']
            del df['new_deaths_without_positive_test']
            del df['new_deaths_total']

            for x in range(len(df['date'])):
                # df_1 = df.copy()
                df['date'][x] = df['date'][x].replace('/', '-')
                df['date'][x] = datetime.datetime.strptime(df['date'][x], '%d-%m-%Y')

            figure.set_figwidth(18)
            figure.set_figheight(6)
            plt.title('Covid-19 Deaths per English Region.')
            region = df['nhs_england_region'][i]
            print(region)
            df_len = len(df) - 1
            x_y = (df['date'][df_len], df['cumulative_deaths_total'][df_len])
            plt.annotate(text=region, xy=x_y)
            plt.plot(df['date'], df['cumulative_deaths_total'])

        print('saving graph')
        plt.savefig(save_path)
        print(f'Graph saved at: {save_path}')
