import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.review import Review

class TestReview(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.review = Review(place_id="1", user_id="1", text="This place was amazing!")

    def test_initialization(self):
        """Test initialization of Review instance."""
        self.assertTrue(hasattr(self.review, 'id'))
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertIsInstance(self.review.id, str)
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)
        self.assertEqual(self.review.place_id, "1")
        self.assertEqual(self.review.user_id, "1")
        self.assertEqual(self.review.text, "This place was amazing!")

    def test_str_representation(self):
        """Test __str__ method of Review."""
        string_representation = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), string_representation)

    def test_save_method(self):
        """Test save method of Review."""
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(old_updated_at, self.review.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of Review."""
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['id'], self.review.id)
        self.assertEqual(review_dict['created_at'], self.review.created_at.isoformat())
        self.assertEqual(review_dict['updated_at'], self.review.updated_at.isoformat())
        self.assertEqual(review_dict['place_id'], self.review.place_id)
        self.assertEqual(review_dict['user_id'], self.review.user_id)
        self.assertEqual(review_dict['text'], self.review.text)

    def tearDown(self):
        """Clean up after tests."""
        del self.review

if __name__ == '__main__':
    unittest.main()
