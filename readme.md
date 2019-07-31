# Rhyme helper

Poetry is a lot of fun, but I always had a tough time of finding the perfect word to use to create end rhyme. I'm a man with a standard vocabulary but an urge to expand, so to get access to new words I've created this project.
It's all based around Google's wonderful pygtrie library. Of the notable data structures that don't natively exist in the python standard library the trie is one.

I'm very happy with how this all came together. It was less than an hour to create, and I now have a helpful command line utility for finding **exactly** the right word.

## Set up

```
$ git clone https://github.com/benjamin-weller/rhyme_helper.git
$ sudo apt-get install --reinstall wamerican
$ cd rhyme_helper
$ cp /usr/share/dict/words words.txt
$ python populate.py
```

## Usage

```$ python poetry.py get <word_in_need_of_rhyme>```
