import unittest
from vaccination.vaccination import Vaccination
from vaccination.download import Download
import os.path
from os import path

class TestVaccination(unittest.TestCase):

    def setUp(self):
       self.vaccination = Vaccination()
       self.download = Download()

    def test_download_bundesweit(self):
        self.download.download_bundesweit("")
        self.assertTrue(path.exists('germany_vaccinations_timeseries_v2.tsv'))


if __name__ == '__main__':
    unittest.main()