import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    
    def setUp(self):
        """Set up the test environment."""
        self.amenity = Amenity(name="Pool")

    def test_initialization(self):
        """Test initialization of Amenity instance."""
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)
        self.assertEqual(self.amenity.name, "Pool")

    def test_str_representation(self):
        """Test __str__ method of Amenity."""
        string_representation = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), string_representation)

    def test_save_method(self):
        """Test save method of Amenity."""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of Amenity."""
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], self.amenity.id)
        self.assertEqual(amenity_dict['created_at'], self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'], self.amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict['name'], self.amenity.name)

    def tearDown(self):
        """Clean up after tests."""
        del self.amenity

if __name__ == '__main__':
    unittest.main()
