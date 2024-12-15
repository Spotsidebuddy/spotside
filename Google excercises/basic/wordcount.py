#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys
from operator import itemgetter
from string import punctuation

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
def print_words(filename) -> None:
    """Prints all words in text ad their count"""
    text: list = import_words(filename)
    unsorted_words_list = clean_words(text)
    counted_words = sorted(count_words(unsorted_words_list).items())
    for item in counted_words:
        print(f'{item[0]} {item[1]}')


def print_top(filename):
    text: list = import_words(filename)
    unsorted_words_list = clean_words(text)
    counted_words = sorted(count_words(unsorted_words_list).items(), key=itemgetter(1), reverse=True)
    for i in range(20):
        print(f'{counted_words[i][0]} {counted_words[i][1]}')




def import_words(filename):
    """gets words from text file splitting them at ' ', words need cleaning afterwards"""
    word_list =[]
    with open(filename, 'r') as f:
        text = f.read().split()
    word_list = clean_words(text)
    return word_list


def clean_words(text):
    """cleans word from list of words with punctuation from said punctuation"""
    word_list = []
    for word in text:
        clean_word = ''
        for char in word:
            if char not in punctuation:
                clean_word += char.lower()
        if word != '' and not word.isnumeric():
            word_list.append(clean_word)
    return word_list

def count_words(word_list):
    """count words in list of words"""
    word_count = {}
    for word in word_list:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return word_count


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
