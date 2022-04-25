import unittest
import os

from linear_regression import regression
import import_data


class MyTestCase(unittest.TestCase):

    data = import_data.ImportData()

    def test_scatter_monthly_new(self):
        data = self.data
        data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\deaths_against_downloads_per_month.csv')
        reg = regression.LinearRegression()
        save_path = f'{os.getcwd()}\\..\\graphs\\deaths_per_download_monthly_new.png'
        reg.create_scatter_graph(data_frame, save_path, 'new_deaths', 'new_downloads')
        self.assertEqual(True, True)

    def test_scatter_weekly_new(self):
        data = self.data
        data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\weekly_deaths_by_downloads.csv')
        reg = regression.LinearRegression()
        save_path = f'{os.getcwd()}\\..\\graphs\\deaths_per_download_weekly.png'
        reg.create_scatter_graph(data_frame, save_path, 'new_deaths', 'new_downloads')
        self.assertEqual(True, True)

    def test_linear_regression_monthly_new(self):
        data = self.data
        data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\deaths_against_downloads_per_month.csv')
        reg = regression.LinearRegression()
        reg.apply(data_frame, 'new_deaths', 'new_downloads')
        self.assertEqual(True, True)

    def test_linear_regression_weekly_new(self):
        data = self.data
        data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\weekly_deaths_by_downloads.csv')
        reg = regression.LinearRegression()
        reg.apply(data_frame, 'new_deaths', 'new_downloads')
        self.assertEqual(True, True)

    def test_scatter_monthly_new_no_outlier(self):
        data = self.data
        data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\deaths_against_downloads_per_month_no_outlier.csv')
        reg = regression.LinearRegression()
        save_path = f'{os.getcwd()}\\..\\graphs\\deaths_per_download_monthly_new_no_outlier.png'
        reg.create_scatter_graph(data_frame, save_path, 'new_deaths', 'new_downloads')
        self.assertEqual(True, True)

    def test_scatter_weekly_new_no_outlier(self):
        data = self.data
        data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\weekly_deaths_by_downloads_no_outlier.csv')
        reg = regression.LinearRegression()
        save_path = f'{os.getcwd()}\\..\\graphs\\deaths_per_download_weekly_no_outlier.png'
        reg.create_scatter_graph(data_frame, save_path, 'new_deaths', 'new_downloads')
        self.assertEqual(True, True)

    def test_linear_regression_monthly_new_no_outlier(self):
        data = self.data
        data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\deaths_against_downloads_per_month_no_outlier.csv')
        reg = regression.LinearRegression()
        reg.apply(data_frame, 'new_deaths', 'new_downloads')
        self.assertEqual(True, True)

    def test_linear_regression_weekly_new_no_outlier(self):
        data = self.data
        data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\weekly_deaths_by_downloads_no_outlier.csv')
        reg = regression.LinearRegression()
        reg.apply(data_frame, 'new_deaths', 'new_downloads')
        self.assertEqual(True, True)

    def test_scatter_monthly_cumulative(self):
        data = self.data
        data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\deaths_against_downloads_per_month.csv')
        reg = regression.LinearRegression()
        save_path = f'{os.getcwd()}\\..\\graphs\\deaths_per_download_monthly_cumulative.png'
        reg.create_scatter_graph(data_frame, save_path, 'cumulative_deaths', 'cumulative_downloads')
        self.assertEqual(True, True)

    def test_scatter_weekly_cumulative(self):
        data = self.data
        data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\weekly_deaths_by_downloads.csv')
        reg = regression.LinearRegression()
        save_path = f'{os.getcwd()}\\..\\graphs\\deaths_per_download_weekly_cumulative.png'
        reg.create_scatter_graph(data_frame, save_path, 'cumulative_deaths', 'cumulative_downloads')
        self.assertEqual(True, True)

    def test_linear_regression_monthly_cumulative(self):
        data = self.data
        data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\deaths_against_downloads_per_month.csv')
        reg = regression.LinearRegression()
        reg.apply(data_frame, 'cumulative_deaths', 'cumulative_downloads')
        self.assertEqual(True, True)

    def test_linear_regression_weekly_cumulative(self):
        data = self.data
        data_frame = data.read_csv(f'{os.getcwd()}\\..\\data\\weekly_deaths_by_downloads.csv')
        reg = regression.LinearRegression()
        reg.apply(data_frame, 'cumulative_deaths', 'cumulative_downloads')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
