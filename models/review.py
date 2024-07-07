from models.base_model import BaseModel

class Review(BaseModel):
    """
    Represents a review.

    Attributes:
        place_id (str): The ID of the place where the review is about.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text of the review.
    """

    def __init__(self, place_id: str, user_id: str, text: str):
        """
        Initializes a new Review instance.

        Args:
            place_id (str): The ID of the place where the review is about.
            user_id (str): The ID of the user who wrote the review.
            text (str): The text of the review.
        """
        super().__init__()
        self.place_id = place_id
        self.user_id = user_id
        self.text = text
