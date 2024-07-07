from base_model import BaseModel

class Amenity(BaseModel):
    """
    Amenity class that inherits from BaseModel.

    Attributes:
        name (str): The name of the amenity.

    Method resolution order:
        |-- Amenity
        |-- BaseModel
    """

    def __init__(self, name: str = ''):
        """
        Initialize an instance of the Amenity class.

        Args:
            name (str, optional): The name of the amenity. Defaults to an empty string.
        """
        super().__init__()
        self.name = name
