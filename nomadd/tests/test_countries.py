import unittest

from models.countries import Countries

class TestCountries(unittest.TestCase):
    def setUp(self):
        self.Country1 = Countries("Ireland", None)


    def test_destination_name(self):
        self.assertEqual("Ireland", self.Country1.country_name)
    def test_destination_id(self):
        self.assertEqual(None, self.Country1.id)