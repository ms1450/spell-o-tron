"""
CSCI-141 Project Spellotron
By Mehul Sen
This Project contains two python files and two text files that are required to run it, an optional third text file
can be created by the user and run through this program.
"""
import sys
from punct import *
from speller import *
LEGAL_WORD_FILE = 'american-english.txt'
KEY_ADJACENCY_FILE = 'keyboard-letters.txt'
g = ['good']
b = ['bad']
dictionary = set()
getdata(LEGAL_WORD_FILE)

"""
USAGE should be as follows : 
python3.7 spellotron.py words/lines [filename]
"""


def main():
    """
    This function reads the entered configuration and allows the program to make choices based on those configurations.
    It is also the main function that runs.
    :return:
    """
    if len(sys.argv) < 2:
        print("Usage = python3.7 spellotron.py words/lines [filename]")
    elif len(sys.argv) == 2:
        if sys.argv[1] == 'words':
            words("")
        elif sys.argv[1] == 'lines':
            lines("")
        else:
            print("Usage = python3.7 spellotron.py words/lines [filename]")
    elif len(sys.argv) == 3:
        if sys.argv[1] == 'words':
            words(sys.argv[2])
        elif sys.argv[1] == 'lines':
            lines(sys.argv[2])
        else:
            print("Usage = python3.7 spellotron.py words/lines [filename]")
    else:
        print("Usage = python3.7 spellotron.py words/lines [filename]")


def words(val):
    """
    This function handles the output if the user chooses the 'word' configuration.
    :param val:
    :return:
    """
    if val == "":
        strInput = input("")
        words = strInput.split()
        length, changes, wrong, correct, sentence, movement = punctuation(words)
    else:
        words = []
        with open(val) as fd:
            for line in fd:
                word = line.strip()
                lst = word.split()
                words = words + lst
        fd.close()
        length, changes, wrong, correct, sentence, movement = punctuation(words)
    for x in movement:
        print(x)
    print(length, 'words read.')
    print("")
    print(len(changes), "Corrected Words")
    print(changes)
    print("")
    print(len(wrong), "Unknown Words")
    print(wrong)


def lines(val):
    """
    This function handles the output if the user choses the 'line' configuration.
    :param val:
    :return:
    """
    if val == "":
        strInput = input("")
        words = strInput.split()
        length, changes, wrong, correct, sentence, movement = punctuation(words)
    else:
        words = []
        with open(val) as fd:
            for line in fd:
                word = line.strip()
                lst = word.split()
                words = words + lst
        fd.close()
        length, changes, wrong, correct, sentence, movement = punctuation(words)
    for x in sentence:
        print(x, end=' ')
    print("")
    print(length, 'words read.')
    print("")
    print(len(changes), "Corrected Words")
    print(changes)
    print("")
    print(len(wrong), "Unknown Words")
    print(wrong)


def punctuation(lst):
    """
    This function calls punct.py and handles punctuation.
    :param lst:
    :return:
    """
    good = []
    wrong = []
    modified = []
    sentence = []
    movement = []
    for x in lst:
        ans = prelim(x)
        if len(ans) is 1:
            if ans[0] == 'good':
                good.append(x)
                sentence.append(x)
            elif ans[0] == 'bad':
                wrong.append(x)
                sentence.append(x)
        elif len(ans) is 2:
            modified.append(ans[0])
            movement.append(ans[1])
            sentence.append(ans[0])
        else:
            print("ERROR - Something Went Terribly Wrong.", file=sys.stderr)
    return len(lst), modified, wrong, good, sentence, movement


if __name__ == '__main__':
    main()
