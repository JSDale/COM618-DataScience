import unittest
import os

from linear_regression import regression
import import_data


class MyTestCase(unittest.TestCase):

    def test_scatter(self):
        data = import_data.ImportData()
        # data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\deaths_against_downloads_per_month.csv')
        data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\deaths_against_downloads_per_month.csv')
        reg = regression.LinearRegression()
        save_path = f'{os.getcwd()}\\..\\graphs\\deaths_per_download_monthly'
        reg.create_scatter_graph(data_frame, save_path)
        self.assertEqual(True, True)

    def test_linear_regression(self):
        data = import_data.ImportData()
        # data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\deaths_against_downloads_per_month.csv')
        data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\weekly_deaths_by_downloads.csv')
        reg = regression.LinearRegression()
        reg.apply(data_frame)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
