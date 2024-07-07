import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.place = Place(city_id="1", user_id="1", name="Cozy Apartment",
                           description="A comfortable apartment in the heart of the city.",
                           number_rooms=2, number_bathrooms=1,
                           max_guest=4, price_by_night=100.0,
                           latitude=37.7749, longitude=-122.4194,
                           amenity_ids=["wifi", "parking"])

    def test_initialization(self):
        """Test initialization of Place instance."""
        self.assertTrue(hasattr(self.place, 'id'))
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertIsInstance(self.place.id, str)
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertEqual(self.place.city_id, "1")
        self.assertEqual(self.place.user_id, "1")
        self.assertEqual(self.place.name, "Cozy Apartment")
        self.assertEqual(self.place.description, "A comfortable apartment in the heart of the city.")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100.0)
        self.assertEqual(self.place.latitude, 37.7749)
        self.assertEqual(self.place.longitude, -122.4194)
        self.assertEqual(self.place.amenity_ids, ["wifi", "parking"])

    def test_str_representation(self):
        """Test __str__ method of Place."""
        string_representation = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), string_representation)

    def test_save_method(self):
        """Test save method of Place."""
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(old_updated_at, self.place.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of Place."""
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], self.place.id)
        self.assertEqual(place_dict['created_at'], self.place.created_at.isoformat())
        self.assertEqual(place_dict['updated_at'], self.place.updated_at.isoformat())
        self.assertEqual(place_dict['city_id'], self.place.city_id)
        self.assertEqual(place_dict['user_id'], self.place.user_id)
        self.assertEqual(place_dict['name'], self.place.name)
        self.assertEqual(place_dict['description'], self.place.description)
        self.assertEqual(place_dict['number_rooms'], self.place.number_rooms)
        self.assertEqual(place_dict['number_bathrooms'], self.place.number_bathrooms)
        self.assertEqual(place_dict['max_guest'], self.place.max_guest)
        self.assertEqual(place_dict['price_by_night'], self.place.price_by_night)
        self.assertEqual(place_dict['latitude'], self.place.latitude)
        self.assertEqual(place_dict['longitude'], self.place.longitude)
        self.assertEqual(place_dict['amenity_ids'], self.place.amenity_ids)

    def tearDown(self):
        """Clean up after tests."""
        del self.place

if __name__ == '__main__':
    unittest.main()
