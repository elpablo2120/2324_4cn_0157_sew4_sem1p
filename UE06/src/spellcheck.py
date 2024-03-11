"""
__author__ = "Paul Waldecker"
__email__ = "0157@htl.rennweg.at"
__version__ = "1.0.0"
__copyright__ = "Copyright 2024"
__license__ = "GPL"
__status__ = "Development"
"""
from typing import Set, List, Tuple, Counter


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
    delete_one = {head + tail[1:] for head, tail in word_splits if len(tail)}

    # Fall b) Zwei Buchstaben verdreht
    transpose_two = {head + tail[1] + tail[0] + tail[2:] for head, tail in word_splits if len(tail) > 1}

    # Fall c) Ein Buchstabe ersetzt
    replace_one = {head + char + tail[1:] for head, tail in word_splits for char in 'abcdefghijklmnopqrstuvwxyz' if len(tail) > 1}

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

def edit2_good(wort: str, alle_woerter: List[str]) -> Set[str]:
    '''
    Finde alle Wörter mit Edit-Distanz zwei. Dazu wird edit1 zweimal aufgerufen.
    :param wort: Das Eingangswort.
    :param alle_woerter: Die Liste aller Wörter.
    :return: Menge aller Wörter mit Edit-Distanz zwei.
    '''
    # Step 1: Calculate edit distance one for the input word
    edit1_result = edit1(wort.lower())

    # Step 2: Calculate edit distance one for each word in the edit1_result
    edit2_result = set()
    for word in edit1_result:
        edit2_result.update(edit1(word.lower()))

    # Step 3: Filter the results to keep only the words in the word list
    valid_edit2_words = set(edit2_result) & set(alle_woerter)

    return valid_edit2_words

def correct(word: str, alle_woerter: List[str]) -> Set[str]:
    """
    Find the correction(s) for the given word based on the specified criteria:
    - If the word is in the word list, return a set with the word.
    - If at least one word with Edit-Distance one is in the word list, return a set of those words.
    - If at least one word with Edit-Distance two is in the word list, return a set of those words.
    - If the word is unknown or has too many errors, return a set with the original word.

    :param word: The input word to be corrected.
    :param alle_woerter: The list of all words in the dictionary.
    :return: A set of corrected words based on the specified criteria.
    """
    # Check if the word is in the word list
    if word.lower() in alle_woerter:
        return {word.lower()}

    # Check for Edit-Distance one corrections
    edit1_result = edit1(word.lower())
    valid_edit1_words = set(edit1_result) & set(alle_woerter)
    if valid_edit1_words:
        return valid_edit1_words

    # Check for Edit-Distance two corrections
    edit2_result = edit2_good(word.lower(), alle_woerter)
    if edit2_result:
        return edit2_result

    # Return the original word if no corrections are found
    return {word.lower()}

# Additional improvement: Sorting corrections based on word frequencies in the dictionary
def correct_sorted(word: str, alle_woerter: List[str]) -> List[str]:
    """
    Find the correction(s) for the given word and sort them based on word frequencies.

    :param word: The input word to be corrected.
    :param alle_woerter: The list of all words in the dictionary.
    :param frequencies: A Counter object containing word frequencies.
    :return: A sorted list of corrected words based on frequencies.
    """
    corrections = list(correct(word, alle_woerter))

    # Sort the corrections based on word frequencies
    sorted_corrections = sorted(corrections, key=lambda , reverse=True)

    return sorted_corrections

filename = '/Users/paulwaldecker/Desktop/HTL3R/4CN/SEW/Angaben/06_py_comprehension/de-en.txt'
word_set = read_all_words(filename)


print(correct('haloo', word_set))

print(correct_sorted("Aalsuppe", word_set, ))  # Output: {'aalsuppe'}
print(correct_sorted("Alsuppe", word_set))  # Output: {'aalsuppe'}
print(sorted(correct_sorted("Alsupe", word_set)))  # Output: ['aalsuppe', 'absude', 'alse', 'lupe']
