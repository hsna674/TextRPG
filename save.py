import pickle
import os
from settings import SAVE_DIRECTORY

class SaveFiles:
    @staticmethod
    def _ensure_directory_exists() -> None:
        """Ensure that the save directory exists; if not, create it."""
        if not os.path.exists(SAVE_DIRECTORY):
            os.makedirs(SAVE_DIRECTORY)

    @staticmethod
    def new_save(data) -> str:
        """Save new data to a new file.

        Args:
            data: The data to be saved.

        Returns:
            str: The name of the newly created save file.
        """
        SaveFiles._ensure_directory_exists()
        file_count = len(os.listdir(SAVE_DIRECTORY))
        file_name = f"save{file_count}"
        with open(os.path.join(SAVE_DIRECTORY, f"{file_name}.pickle"), "wb") as f:
            pickle.dump(data, f)
        return file_name

    @staticmethod
    def save(data, file_name: str) -> None:
        """Save data to a specified file.

        Args:
            data: The data to be saved.
            file_name (str): The name of the file to save to.
        """
        SaveFiles._ensure_directory_exists()
        file_path = os.path.join(SAVE_DIRECTORY, f"{file_name}.pickle")
        with open(file_path, "wb") as f:
            pickle.dump(data, f)

    @staticmethod
    def load(file_name: str) -> dict:
        """Load data from a specified file.

        Args:
            file_name (str): The name of the file to load data from.

        Returns:
            dict: The loaded data.
        
        Raises:
            FileNotFoundError: If the specified file does not exist.
        """
        file_path = os.path.join(SAVE_DIRECTORY, f"{file_name}.pickle")
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_name}.pickle' not found.")
        with open(file_path, "rb") as f:
            return pickle.load(f)
