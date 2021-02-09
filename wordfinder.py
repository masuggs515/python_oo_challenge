"""Word Finder: finds random words from a dictionary."""
from random import choice as pick

class WordFinder:
    """
    takes list of words (if every word is on their own line) and finds a random word in the list

    >>> w = WordFinder("test.txt")

    >>> w.random_word() in ["#banana", "#fail", "apple", "banana", "tree"]
    True

    >>> w.random_word() in ["#banana", "#fail", "apple", "banana", "tree"]
    True

    >>> w.random_word() in ["#banana", "#fail", "apple", "banana", "tree"]
    True
    """
    def __init__(self, path):
        file = open(path, "r")
        self.words = self.read_file(file)
        

    def read_file(self, file):
        """
        read file and create list of all lines
        """
        
        return [s.strip('\n') for s in file]

    def random_word(self):
        """ find and return random word from file"""
        return pick(self.words)


class SpecialWordFinder(WordFinder):  
    """
    Filters out any lines that are comments (start with #) or are empty lines

    >>> x = SpecialWordFinder('test.txt')

    >>> x.random_word() in ["apple", "banana", "tree"]
    True

    >>> x.random_word() in ["apple", "banana", "tree"]
    True

    >>> x.random_word() in ["#banana", "#fail"]
    False
    """      

    def read_file(self, file):

        return [x.strip() for x in file if not x.startswith("#") and x.strip()]
        