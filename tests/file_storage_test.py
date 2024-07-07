import unittest
import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models import storage

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.base_model = BaseModel()
        self.user = User(email="test@example.com", password="securepassword", first_name="John", last_name="Doe")
        self.place = Place(city_id="1", user_id="1", name="Cozy Apartment", description="A nice place to stay",
                           number_rooms=2, number_bathrooms=1, max_guest=4, price_by_night=100.0,
                           latitude=40.7128, longitude=-74.0060)
        self.amenity = Amenity(name="WiFi")
        self.city = City(state_id="1", name="New York")
        self.state = State(name="New York")
        self.review = Review(place_id="1", user_id="1", text="Great place to stay!")

    def tearDown(self):
        """Clean up after tests."""
        storage.reload()
        del self.base_model
        del self.user
        del self.place
        del self.amenity
        del self.city
        del self.state
        del self.review

    def test_all_method(self):
        """Test the all method of FileStorage."""
        all_objects = storage.all()
        self.assertTrue(isinstance(all_objects, dict))
        self.assertIn(f"BaseModel.{self.base_model.id}", all_objects)
        self.assertIn(f"User.{self.user.id}", all_objects)
        self.assertIn(f"Place.{self.place.id}", all_objects)
        self.assertIn(f"Amenity.{self.amenity.id}", all_objects)
        self.assertIn(f"City.{self.city.id}", all_objects)
        self.assertIn(f"State.{self.state.id}", all_objects)
        self.assertIn(f"Review.{self.review.id}", all_objects)

    def test_new_method(self):
        """Test the new method of FileStorage."""
        new_model = BaseModel()
        storage.new(new_model)
        key = f"BaseModel.{new_model.id}"
        self.assertIn(key, storage.all())

    def test_save_method(self):
        """Test the save method of FileStorage."""
        new_model = BaseModel()
        new_model.save()
        storage.reload()  # Reload to ensure saved data is loaded from file
        key = f"BaseModel.{new_model.id}"
        self.assertIn(key, storage.all())

    def test_reload_method(self):
        """Test the reload method of FileStorage."""
        initial_objects = storage.all()
        storage.save()
        storage.reload()
        reloaded_objects = storage.all()
        self.assertEqual(initial_objects, reloaded_objects)

if __name__ == '__main__':
    unittest.main()
