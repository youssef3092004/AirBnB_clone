import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    
    def setUp(self):
        """Set up the test environment."""
        self.model = BaseModel()

    def test_initialization(self):
        """Test initialization of BaseModel instance."""
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        """Test __str__ method of BaseModel."""
        string_representation = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), string_representation)

    def test_save_method(self):
        """Test save method of BaseModel."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method of BaseModel."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertTrue(all(key in model_dict.keys() for key in self.model.__dict__.keys()))

    def test_kwargs_initialization(self):
        """Test initialization of BaseModel instance with kwargs."""
        data = {
            'id': '1234',
            'created_at': '2023-01-01T00:00:00',
            'updated_at': '2023-01-01T00:00:00',
            'name': 'Test Model'
        }
        model_with_kwargs = BaseModel(**data)
        self.assertEqual(model_with_kwargs.id, data['id'])
        self.assertEqual(model_with_kwargs.created_at.isoformat(), data['created_at'])
        self.assertEqual(model_with_kwargs.updated_at.isoformat(), data['updated_at'])
        self.assertEqual(model_with_kwargs.name, data['name'])

    def tearDown(self):
        """Clean up after tests."""
        del self.model

if __name__ == '__main__':
    unittest.main()
