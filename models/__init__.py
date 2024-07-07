from imp import reload
from .engine import file_storage

def initialize_storage():
    """
    Initializes the file storage system.

    Returns:
    A FileStorage object that represents the file storage system.
    """
    storage = file_storage.FileStorage()
    return storage

def reload_storage(storage):
    """
    Reloads the file storage system.

    Parameters:
    storage (FileStorage): The FileStorage object to be reloaded.

    Returns:
    The reloaded FileStorage object.
    """
    return reload(storage)
