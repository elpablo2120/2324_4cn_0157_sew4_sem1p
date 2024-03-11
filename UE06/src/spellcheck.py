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

def edit1(wort: str) -> Set[str]:
    """
    Finde alle Wörter mit Edit-Distanz eins (= ein Tippfehler).
    :param wort: Das Eingangswort.
    :return: Menge aller Wörter mit Edit-Distanz eins.
    """
    word_splits = split_word(wort)

    # Fall a) Ein Buchstabe fehlt
    delete_one = {head + tail[1:] for head, tail in word_splits if tail}

    # Fall b) Zwei Buchstaben verdreht
    transpose_two = {head + tail[1] + tail[0] + tail[2:] for head, tail in word_splits if len(tail) > 1}

    # Fall c) Ein Buchstabe ersetzt
    replace_one = {head + char + tail[1:] for head, tail in word_splits for char in 'abcdefghijklmnopqrstuvwxyz'}

    # Fall d) Ein Buchstabe eingefügt
    insert_one = {head + char + tail for head, tail in word_splits for char in 'abcdefghijklmnopqrstuvwxyz'}

    # Kombiniere alle Möglichkeiten in einem Set und gebe es zurück
    result_set = delete_one | transpose_two | replace_one | insert_one
    return result_set

def edit1_good(wort: str, alle_woerter:List[str]) -> Set[str]:
    '''
    Ruft edit1 auf und filtert nach Wörtern die in der Liste alle_woerter enthalten sind.
    :param wort:
    :param alle_woerter:
    :return:
    '''
    edit1_result = edit1(wort.lower())

    # Filtern der Ergebnisse, um nur die Wörter im Wörterbuch zu behalten
    return set(edit1_result) & set(alle_woerter)

def edit2_good(wort:str, alle_woerter:List[str]) -> Set[str]:
    '''
    Finde alle Wörter mit Edit-Distanz zwei. Dazu wird edit1 zweimal aufgerufen.
    :param wort:
    :param alle_woerter:
    :return:
    '''
    for i in range(2):
        wort = edit1_good(wort, alle_woerter)
        return wort
    return set(wort)


# Beispiel
example_word = "haalo"
result = edit1(example_word)
#print(result)



# Beispielaufruf:
filename = '/Users/paulwaldecker/Desktop/HTL3R/4CN/SEW/Angaben/06_py_comprehension/de-en.txt'
word_set = read_all_words(filename)
#print(split_word('abc'))
#print(word_set)

resultedit2 = edit2_good('hhallo', word_set)
print(resultedit2)
