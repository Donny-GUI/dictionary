import os
import csv


dsyms = {
    "n.": "noun",
    "N.": "noun",
    "sing.": "singular",
    "sing": "singular",
    "Sing": "singlular",
}

DICT_CSV = os.path.join(os.path.dirname(__file__), "entries.csv")


def read_english_dictionary():
    with open(DICT_CSV, mode="r") as file:
        csv_reader = csv.reader(file)
        rows = [x for x in csv_reader]
    return rows