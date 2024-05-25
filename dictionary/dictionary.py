import time
from random import randint
from typing import List, Dict
from .type import Entries, entry, WordType
from .settings import read_english_dictionary
from .handler import DictionaryHandler


class Dictionary:
    def __init__(self) -> None:
        """
        Initializes the Dictionary object, reads the English dictionary data,
        and organizes it into a dictionary structure for fast lookups.

        Attributes:
            columns (int): Number of columns in the dictionary data.
            symbols (List[str]): List of symbols used in the dictionary.
            _dict (Dict[str, Entries]): Dictionary data organized by the first letter of each word.
            data (List[tuple]): Raw dictionary data read from an external source.
            rows (int): Number of rows in the dictionary data.
        """
        self.columns = 9
        self.symbols = []
        self._dict: Dict[str, Entries] = {}

        _start = time.time()
        self.data = read_english_dictionary()
        self.rows = len(self.data)

        for row in self.data:
            e = entry(*row)
            try:
                self._dict[row[1][0]].append(e)
            except KeyError:
                self._dict[row[1][0]] = [e]

        _d = time.time() - _start
        print("Dictionary Load time: ", _d)
    
    def _load(self):

    
    def definitions(self, word: str) -> List[str]:
        """
        Get the definitions of a word.

        Args:
            word (str): The word to look up.

        Returns:
            List[str]: A list of definitions for the given word.
        """
        _word = word.lower()
        return [x.definition for x in self._dict.get(_word[0], []) if x.word.lower() == _word]
    
    def wordtypes(self, word: str) -> List[WordType]:
        """
        Get the word types (parts of speech) of a word.

        Args:
            word (str): The word to look up.

        Returns:
            List[WordType]: A list of word types for the given word.

        Raises:
            Exception: If the first character of the word is not recognized.
        """
        _word = word.lower()
        try:
            return [e.wtype for e in self._dict[_word[0]] if e.word.lower() == _word]
        except IndexError:
            raise Exception("Does not recognize first character in word")
        except KeyError:
            return []

    def random(self) -> entry:
        """
        Get a random entry from the dictionary.

        Returns:
            entry: A random dictionary entry.
        """
        rr = randint(0, self.rows - 1)
        return self.data[rr]

    def lookup(self, word: str) -> List[entry]:
        """
        Look up a word and get all entries that match the word.

        Args:
            word (str): The word to look up.

        Returns:
            List[entry]: A list of dictionary entries for the given word.
        """
        _word = word.lower()
        return [e for e in self._dict.get(_word[0], []) if e.word.lower() == _word]

    def __call__(self):
        return DictionaryHandler.load("dictionary.serial")
