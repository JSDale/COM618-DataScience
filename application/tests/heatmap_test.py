import unittest
import os
from plotting import heat_map as hm


class HeatmapTests(unittest.TestCase):

    def test_hetmap_is_created(self):
        filepath = f'{os.getcwd()}\\..\\data\\DeathsPerLocationPerDate.json'
        plotting = hm.HeathMapPlotting()
        plotting.plot(filepath)
