import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.user = User(email="test@example.com", password="securepassword", first_name="John", last_name="Doe")

    def test_initialization(self):
        """Test initialization of User instance."""
        self.assertTrue(hasattr(self.user, 'id'))
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertIsInstance(self.user.id, str)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "securepassword")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_str_representation(self):
        """Test __str__ method of User."""
        string_representation = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), string_representation)

    def test_save_method(self):
        """Test save method of User."""
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(old_updated_at, self.user.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of User."""
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['created_at'], self.user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'], self.user.updated_at.isoformat())
        self.assertEqual(user_dict['email'], self.user.email)
        self.assertEqual(user_dict['password'], self.user.password)
        self.assertEqual(user_dict['first_name'], self.user.first_name)
        self.assertEqual(user_dict['last_name'], self.user.last_name)

    def tearDown(self):
        """Clean up after tests."""
        del self.user

if __name__ == '__main__':
    unittest.main()
