import unittest

from the_race.read_file_race import ReadFileRace
from .variables_test import var_to_list

class ReadFileRaceTests(unittest.TestCase):
    def setUp(self):
        self.to_list = var_to_list
    def test_file_not_exist(self):
        path = "/.tests/llll"
        with self.assertRaises(FileExistsError):
            ReadFileRace(path)

    def test_file_property_to_list(self):
        path = "./race.log"
        self.assertEqual(self.to_list, ReadFileRace(path).to_list)
