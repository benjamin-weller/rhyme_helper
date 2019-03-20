import pygtrie as trie
import os
import pickle

backwards_words = trie.CharTrie()

"""
'r'   This is the default mode. It Opens file for reading.

'w'   This Mode Opens file for writing.
      If file does not exist, it creates a new file.
      If file exists it truncates the file.

'x'   Creates a new file. If file already exists, the operation fails.

'a'   Open file in append mode.
      If file does not exist, it creates a new file.

't'   This is the default mode. It opens in text mode.

'b'   This opens in binary mode.

'+'   This will open a file for reading and writing (updating)
"""
lines = None
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "words.txt"), 'r') as file:
    lines = file.readlines()
for x in lines:
    # Make it lower case, then exclude the pesky \n at the end
    # then make it backwards
    backwards_words[(x.lower()[:-1])[::-1]] = None

# The backwards trie is now ready
# write it out to a pickle file
import pickle
pickle.dump(backwards_words, open(r'triepickle', 'wb'))