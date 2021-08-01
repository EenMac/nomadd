import unittest

from models.cities import Cities

class TestCities(unittest.TestCase):
    def setUp(self):
        self.City1 = Cities("Dublin", "Ireland", False)

    def test_city_has_name(self):
        self.assertEqual("Dublin", self.City1.city_name)
    
    def test_city_visited(self):
        self.assertEqual(False, self.City1.visited)