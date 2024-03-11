"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""

from typing import Set, List, Tuple


def read_all_words(filename: str) -> set or FileNotFoundError:
    """
    Liest Wörter aus einer Datei ein und speichert sie in einem Set.
    :param filename: Pfad zur Datei
    :return: set mit allen Wörtern aus der Datei
    >>> read_all_words('de-en.txt')
    Die Datei de-en.txt wurde nicht gefunden.
    <class 'FileNotFoundError'>
    >>> read_all_words('/Users/paulwaldecker/Desktop/HTL3R/4CN/SEW/Angaben/06_py_comprehension/test.txt')
    {'paul'}
    """
    word_set = set()

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.split()
                words = {word.lower() for word in words}
                word_set.update(words)
    except FileNotFoundError:
        print(f'Die Datei {filename} wurde nicht gefunden.')
        return FileNotFoundError

    return word_set


def split_word(wort: str) -> List[Tuple[str, str]]:
    """
    Teilt ein Wort in alle möglichen Paare von Wörtern auf. Und speichert sie als Tupel in einer Liste.
    :param wort: Wort das aufgeteilt werden soll
    :return: Liste mit Tupeln von Wörtern
    >>> split_word('Paul')
    [('', 'paul'), ('p', 'aul'), ('pa', 'ul'), ('pau', 'l'), ('paul', '')]
    """
    wort = wort.lower()
    return [(wort[:i], wort[i:]) for i in range(len(wort) + 1)]


def edit1(wort: str) -> Set[str]:
    """
    Finde alle Wörter mit Edit-Distanz eins (= ein Tippfehler).
    :param wort: Das Eingangswort.
    :return: Menge aller Wörter mit Edit-Distanz eins.
    """
    word_splits = split_word(wort)

    # Fall a) Ein Buchstabe fehlt
    delete_one = {head + tail[1:] for head, tail in word_splits if len(tail)}

    # Fall b) Zwei Buchstaben verdreht
    transpose_two = {head + tail[1] + tail[0] + tail[2:] for head, tail in word_splits if len(tail) > 1}

    # Fall c) Ein Buchstabe ersetzt
    replace_one = {head + char + tail[1:] for head, tail in word_splits for char in 'abcdefghijklmnopqrstuvwxyz' if
                   len(tail) > 1}

    # Fall d) Ein Buchstabe eingefügt
    insert_one = {head + char + tail for head, tail in word_splits for char in 'abcdefghijklmnopqrstuvwxyz'}

    result_set = delete_one | transpose_two | replace_one | insert_one
    return result_set


def edit1_good(wort: str, alle_woerter: List[str]) -> Set[str]:
    """
    Ruft edit1 auf und filtert nach Wörtern die in der Liste alle_woerter enthalten sind.
    :param wort: Das Eingangswort.
    :param alle_woerter: Das Wörterbuch.
    :return: Set mit Wörtern, die auch in der Liste alle_woerter enthalten sind.
    >>> alle_woerter = read_all_words('/Users/paulwaldecker/Desktop/HTL3R/4CN/SEW/Angaben/06_py_comprehension/de-en.txt')
    >>> edit1_good('Haalo', alle_woerter)
    {'hallo'}
    """
    edit1_result = edit1(wort.lower())

    return set(edit1_result) & set(alle_woerter)


def edit2_good(wort: str, alle_woerter: List[str]) -> Set[str]:
    """
    Finde alle Wörter mit Edit-Distanz zwei. Dazu wird edit1 zweimal aufgerufen.
    :param wort: Das Eingangswort.
    :param alle_woerter: Die Liste aller Wörter.
    :return: Menge aller Wörter mit Edit-Distanz zwei.
    >>> alle_woerter = read_all_words('/Users/paulwaldecker/Desktop/HTL3R/4CN/SEW/Angaben/06_py_comprehension/de-en.txt')
    >>> edit2_good('Haaloo', alle_woerter)
    {'hallo'}
    """
    edit1_result = edit1(wort.lower())

    edit2_result = set()
    for word in edit1_result:
        edit2_result.update(edit1(word.lower()))

    valid_edit2_words = set(edit2_result) & set(alle_woerter)

    return valid_edit2_words

def correct(word: str, alle_woerter: List[str]) -> Set[str]:
    """
    Findet Korrekturen in einer Liste.
    Entweder:
    - das Wort ist im Wörterbuch (Ergebnis: eine Liste mit einem Eintrag word)
    - oder (mindestens) ein Wort mit Edit-Distanz eins ist im Wörterbuch (Ergebnis: Liste dieser Wörter)
    - oder (mindestens) ein Wort mit Edit-Distanz zwei ist im Wörterbuch (Ergebnis: Liste dieser Wörter)
    - oder wir haben keine Idee (zu viele Fehler oder unbekanntes Wort): liefere eine Liste mit dem ursprünglichen Wort
    :param word: Das Eingangswort.
    :param alle_woerter: Das Wörterbuch.
    :return: Mögliche Korrekturen.
    >>> alle_woerter = read_all_words('/Users/paulwaldecker/Desktop/HTL3R/4CN/SEW/Angaben/06_py_comprehension/de-en.txt')
    >>> correct("Aalsuppe", alle_woerter)
    {'aalsuppe'}
    >>> correct("Alsuppe", alle_woerter)
    {'aalsuppe'}
    >>> sorted(correct("Alsupe", alle_woerter))
    ['aalsuppe', 'absude', 'alse', 'lupe']
    """
    word = word.lower()
    if word in alle_woerter:
        return {word}
    else:
        corrections_edit1 = edit1_good(word, alle_woerter)
        corrections_edit2 = edit2_good(word, alle_woerter)
        return corrections_edit1 or corrections_edit2 or {word}
