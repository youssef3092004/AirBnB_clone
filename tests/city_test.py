import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.city = City(state_id="CA", name="San Francisco")

    def test_initialization(self):
        """Test initialization of City instance."""
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertEqual(self.city.state_id, "CA")
        self.assertEqual(self.city.name, "San Francisco")

    def test_str_representation(self):
        """Test __str__ method of City."""
        string_representation = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), string_representation)

    def test_save_method(self):
        """Test save method of City."""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(old_updated_at, self.city.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of City."""
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['id'], self.city.id)
        self.assertEqual(city_dict['created_at'], self.city.created_at.isoformat())
        self.assertEqual(city_dict['updated_at'], self.city.updated_at.isoformat())
        self.assertEqual(city_dict['state_id'], self.city.state_id)
        self.assertEqual(city_dict['name'], self.city.name)

    def tearDown(self):
        """Clean up after tests."""
        del self.city

if __name__ == '__main__':
    unittest.main()
