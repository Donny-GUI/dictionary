from .dictionary import Dictionary
import pickle


class DictionaryHandler:

    @staticmethod
    def new() -> Dictionary:
        return Dictionary()

    @staticmethod
    def save(dictionary: Dictionary=None) -> None:
        dictionary = Dictionary() if dictionary is None else dictionary
        with open("dictionary.serial", "wb") as f:
            pickle.dump(dictionary, f)
    
    @staticmethod
    def load(dictionary:str=None) -> Dictionary:
        if dictionary is None:
            return Dictionary()
        elif isinstance(dictionary, str):
            with open("dictionary.serial", "rb") as f:
                data = pickle.load(f)
            return data
