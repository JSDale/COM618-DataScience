import pandas as pd

from import_data import ImportData
import os
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import drange


def main():
    import_data = ImportData()
    arr = [
        import_data.read_csv(f'{os.getcwd()}\\data\\EastOfEngland.csv'),
        import_data.read_csv(f'{os.getcwd()}\\data\\London.csv'),
        import_data.read_csv(f'{os.getcwd()}\\data\\Midlands.csv'),
        import_data.read_csv(f'{os.getcwd()}\\data\\NorthEastAndYorkshire.csv'),
        import_data.read_csv(f'{os.getcwd()}\\data\\NorthWest.csv'),
        import_data.read_csv(f'{os.getcwd()}\\data\\SouthEast.csv'),
        import_data.read_csv(f'{os.getcwd()}\\data\\SouthWest.csv'),
    ]

    for i in range(len(arr)):
        df = arr[i]
        del df['new_deaths_with_positive_test']
        del df['new_deaths_without_positive_test']
        del df['new_deaths_total']

        for x in range(len(df['date'])):
            df['date'][x] = df['date'][x].replace('/', '-')
            df['date'][x] = datetime.datetime.strptime(df['date'][x], '%d-%m-%Y')

        plt.title = df['nhs_england_region'][0]
        # plt.plot(df['date'], df['cumulative_deaths_total'])
        figure = plt.figure()
        figure.set_figwidth(18)
        figure.set_figheight(6)
        plt.plot(df['date'], df['cumulative_deaths_total'])

        print('saving graph')
        plt.savefig(f'{os.getcwd()}\\graphs\\test{i}.png')


if __name__ == "__main__":
    main()
