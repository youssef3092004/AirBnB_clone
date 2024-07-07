from base_model import BaseModel

class State(BaseModel):
    """
    A State object represents a geographical region with a unique name.

    Attributes:
        name (str): The name of the state.

    Methods:
        __init__(self, name: str) -> None: Initializes a new State object with the given name.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes a new State object with the given name.

        Args:
            name (str): The name of the state.

        Returns:
            None
        """
        super().__init__()
        self.name = name
