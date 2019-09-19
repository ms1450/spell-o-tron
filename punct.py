"""
CSCI Project Spellotron
By Mehul Sen
This is another helper program to spellotron.py
"""
from speller import *
import string
LEGAL_WORD_FILE = 'american-english.txt'
dictionary = set()
getdata(LEGAL_WORD_FILE)
g = ['good']
b = ['bad']


def remove_punctuation(value):
    """
    This function removes any punctuation present in the code.
    :param value:
    :return:
    """
    result = ""
    pun = False
    for c in value:
        # If char is not punctuation, add it to the result.
        if c not in string.punctuation:
            result += c
        else:
            pun = True
    return result, pun


def prelim(word):
    """
    This is th function that is run bey spellotron and takes care of numbers.
    :param word:
    :return:
    """
    if word.isdigit():
        return g
    elif check(word) is True:
         return g
    else:
        return punc(word)


def punc(word):
    """
    This is the main function that takes case of the punctuation and the caps lock.
    :param word:
    :return:
    """
    word1, dec = remove_punctuation(word)
    if dec is False:
        wordc, stat = caps(word)
        if stat is True and check(wordc) is True:
            return [wordc, word + '-->' + wordc]
        else:
            cword1 = speller(wordc)
            if cword1 is not False:
                return [cword1, word + '-->' + cword1]
            else:
                return b
    else:
        if check(word1) is True:
            return [word1, word + '-->' + word1]
        else:
            wordc, stat = caps(word1)
            if stat is True and check(wordc) is True:
                return [wordc, word + '-->' + wordc]
            elif stat is True:
                cword1 = speller(wordc)
                if cword1 is not False:
                    return [cword1, word + '-->' + cword1]
                else:
                    return b
            else:
                cword1 = speller(word1)
                if cword1 is not False:
                    return [cword1, word + '-->' + cword1]
                else:
                    return b


def caps(word):
    """
    This function handles the puctuation cases and removes it if it is present.
    :param word:
    :return:
    """
    if word[0].isupper():
        front = word[0].lower()
        wordnew = front + word[1:]
        #print(wordnew)
        return wordnew, True
    else:
        return word, False
