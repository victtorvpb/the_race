import unittest

import datetime as dt

from .read_file_race import ReadFileRace
from .the_race import TheRace
from .test_variables import var_process_data, list_total_time


class TheRaceTests(unittest.TestCase):
    def setUp(self):
        self.list_laps = ReadFileRace("ace.log").to_list
        self.the_race = TheRace(self.list_laps)

    def test_process_datas(self):
        self.assertEqual(self.the_race.process_data(), var_process_data)

    def test_total_time(self):

        total_time = total_time = dt.timedelta(seconds=251, microseconds=578000)

        last_lap = dt.datetime.strptime("1:02.769", "%M:%S.%f")
        self.assertEqual(
            self.the_race.calculate_total_time_pilot(list_total_time),
            (total_time, last_lap),
        )
