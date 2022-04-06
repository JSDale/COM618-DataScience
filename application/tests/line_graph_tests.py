import unittest
import os

from plotting import line_graph
from import_data import ImportData
from pre_processing import remove_null_values


class MyTestCase(unittest.TestCase):

    def tests_line_graph_plotting(self):
        lg = line_graph.LineGraphPlotting()
        import_data = ImportData()
        df_arr = [
            import_data.read_csv(f'{os.getcwd()}\\..\\data\\EastOfEngland.csv'),
            import_data.read_csv(f'{os.getcwd()}\\..\\data\\London.csv'),
            import_data.read_csv(f'{os.getcwd()}\\..\\data\\Midlands.csv'),
            import_data.read_csv(f'{os.getcwd()}\\..\\data\\NorthEastAndYorkshire.csv'),
            import_data.read_csv(f'{os.getcwd()}\\..\\data\\NorthWest.csv'),
            import_data.read_csv(f'{os.getcwd()}\\..\\data\\SouthEast.csv'),
            import_data.read_csv(f'{os.getcwd()}\\..\\data\\SouthWest.csv'),
        ]

        null_processor = remove_null_values.RemoveNullValues
        for i in range(len(df_arr)):
            null_processor.drop_not_a_number(df_arr[i])

        save_path = f'{os.getcwd()}\\..\\graphs\\deaths_per_region.png'
        lg.plot(df_arr, save_path)
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
