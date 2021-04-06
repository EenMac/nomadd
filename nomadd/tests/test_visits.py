import unittest
from models.visits import Visits

class TestVisits(unittest.TestCase):
    def setUp(self):
        self.Visits1 = Visits("John", "Dublin", "Would not recommend even to my worst enemies", None)

    def test_user_name(self):
        self.assertEqual("John", self.Visits1.user_name)
    def test_city_has_name(self):
        self.assertEqual("Dublin", self.Visits1.city_name)
    def test_can_review(self):
        self.assertEqual("Would not recommend even to my worst enemies", self.Visits1.review)
    def test_id(self):
        self.assertEqual(None, self.Visits1.id)