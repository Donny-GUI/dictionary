from typing import List, NewType


WordType = NewType('WordType', str)

@dataclass
class entry:
    index:str
    unknown: str
    word: str
    wtype: WordType
    definition: str
    usage: str
    etymology: str
    synonymns: str
    antonyms: str

Entries = NewType('Entries', List[entry])
