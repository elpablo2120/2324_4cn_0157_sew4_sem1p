"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""
from typing import Set, List, Tuple


def read_all_words(filename: str) -> set:
    '''
    Liest Wörter aus einer Datei ein und speichert sie in einem Set.
    :param filename: Pfad zur Datei
    :return: set mit allen Wörtern aus der Datei
    '''
    word_set = set()

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                word_set.update(words)
    except FileNotFoundError:
        print(f'Die Datei {filename} wurde nicht gefunden.')

    return word_set

def split_word(wort:str) -> List[Tuple[str, str]]:
    '''
    Teilt ein Wort in alle möglichen Paare von Wörtern auf. Und speichert sie als Tupel in einer Liste.
    :param wort: Wort das aufgeteilt werden soll
    :return: Liste mit Tupeln von Wörtern
    '''
    return [(wort[:i], wort[i:]) for i in range(len(wort) + 1)]

# Beispielaufruf:
filename = '/Users/paulwaldecker/Desktop/HTL3R/4CN/SEW/Angaben/06_py_comprehension/de-en.txt'
word_set = read_all_words(filename)
print(split_word('hallo'))
#print(word_set)

