from base_model import BaseModel

class City(BaseModel):
    """
    A model representing a city.

    Attributes:
        state_id (str): The ID of the state the city belongs to.
        name (str): The name of the city.
    """

    def __init__(self, state_id: str, name: str):
        """
        Initialize a new City object.

        Args:
            state_id (str): The ID of the state the city belongs to.
            name (str): The name of the city.
        """
        super().__init__()
        self.state_id = state_id
        self.name = name
