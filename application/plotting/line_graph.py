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
                formatted_date = df['date'].iloc[x].replace('/', '-')
                df['date'].iloc[[x]] = datetime.datetime.strptime(formatted_date, '%d-%m-%Y')

            figure.set_figwidth(18)
            figure.set_figheight(6)
            plt.title('Covid-19 Deaths per English Region.')
            region = df['nhs_england_region'][i]
            print(region)
            plt.legend()
            plt.plot(df['date'], df['cumulative_deaths_total'], label=region)
            plt.legend()

        print('saving graph')
        plt.savefig(save_path)
        print(f'Graph saved at: {save_path}')
