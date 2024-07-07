from base_model import BaseModel

class User(BaseModel):
    """
    User model representing a user in the system.

    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """

    def __init__(self, email: str, password: str, first_name: str, last_name: str):
        """
        Initialize a new User instance.

        Args:
            email (str): The user's email address.
            password (str): The user's password.
            first_name (str): The user's first name.
            last_name (str): The user's last name.
        """
        super().__init__()
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
