import unittest
import os

from import_data import ImportData
from pre_processing import combinning_data


class MyTestCase(unittest.TestCase):

    def test_combining(self):
        data = ImportData()
        data_frame_deaths = data.read_csv(f'{os.getcwd()}\\..\\data\\_nhse_total_deaths_by_region.csv')
        data_frame_downloads = data.read_csv(f'{os.getcwd()}\\..\\data\\covid19_app_country_agnostic_dataset.csv')
        com = combinning_data.Combine()
        result = com.deaths_and_downloads(data_frame_deaths, data_frame_downloads)
        for i in range(len(result)):
            print(result[i])
        print(len(result))
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
