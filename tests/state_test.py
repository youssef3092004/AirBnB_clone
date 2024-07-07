import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.state import State

class TestState(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        self.state = State(name="California")

    def test_initialization(self):
        """Test initialization of State instance."""
        self.assertTrue(hasattr(self.state, 'id'))
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertIsInstance(self.state.id, str)
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)
        self.assertEqual(self.state.name, "California")

    def test_str_representation(self):
        """Test __str__ method of State."""
        string_representation = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), string_representation)

    def test_save_method(self):
        """Test save method of State."""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of State."""
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['id'], self.state.id)
        self.assertEqual(state_dict['created_at'], self.state.created_at.isoformat())
        self.assertEqual(state_dict['updated_at'], self.state.updated_at.isoformat())
        self.assertEqual(state_dict['name'], self.state.name)

    def tearDown(self):
        """Clean up after tests."""
        del self.state

if __name__ == '__main__':
    unittest.main()
