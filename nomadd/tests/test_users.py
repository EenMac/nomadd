import unittest
from models.users import Users

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.User1 = Users("James", None)
    
    def test_user_has_name(self):
        self.assertEqual("James", self.User1.user_name)
    
    def test_user_has_id(self):
        self.assertEqual(None, self.User1.id)