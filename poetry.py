"""
Usage:
    poetry.py get <word_in_need_of_rhyme>
"""

from docopt import docopt
import os 
import pickle
import pyperclip

def pickled_trie():
    if os.path.isfile(os.path.join(os.path.dirname(os.path.realpath(__file__)), "triepickle")):
        return pickle.load(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "triepickle"), 'rb'))
    else:
        raise Exception("Looks like there wasn't the pickled trie.")

def get_prefix(string):
    if len(string) <= 2:
        return string
    elif len(string) == 3:
        return string[-2:]
    else:
        return string[-3:]

if __name__ == '__main__':
    arguments = docopt(__doc__)
    my_trie = pickled_trie()

    if "get" in arguments:
        # Get rhyming words out
        string = arguments["<word_in_need_of_rhyme>"]
        # Get the last few letters, now reverse them so they match the last few letters of a rhyming word
        prefix = get_prefix(string)[::-1]
        returned_list = []
        for x in my_trie.items(prefix=prefix):
            # Get the string out of the dictionary element one, and then make it the right way
            returned_list.append((x[0])[::-1])
        # print(returned_list)
        pyperclip.copy(str(returned_list))
