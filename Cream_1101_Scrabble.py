import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # in_file: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # word_list: list of strings
    word_list = []
    for line in in_file:
        word_list.append(line.strip().lower())
    print("  ", len(word_list), "words loaded.")
    return word_list


def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


def get_word_score(word: str, n: int):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """

    # checking pre-cont=dition
    assert isinstance(word, str), "word must be a string"

    if len(word) > 0:
        word = word.lower()
        assert word.islower()
        assert len(word)

    assert isinstance(n, int), "n must be an int"
    assert n > 0, "hand length n must not be 0"


    #Psuedocode

    """
    For each letter in word
        get letter score from dict SCRABBLE_LETTER_VALUES
        add up all the letter scores

    multiply by length of words
    followed by bonus calculation
    example, if n=7 and you make the word 'waybel' on the first try
    it would be worth 115 points
    """
    word_score = 0
    for letter in word:
        word_score += SCRABBLE_LETTER_VALUES[letter]
    word_score *= len(word)
    if len(word) == n:
        word_score += 50

    # checking post-condition
    assert word_score >= 0, "score calculation failed - score is negative"
    assert isinstance(word_score, int), "score must be integer"


    return word_score

# testcase
print(get_word_score("happy", 7))