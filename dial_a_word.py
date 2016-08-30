"""Dial-a-word is a program to generate dictionary words by phone number."""

import itertools
import re

phonepad = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs",
            8: "tuv", 9: "wxyz"}
WORD_FILE = "words2.txt"


def seed_dictionary(textfile):
    """Create a dict that stores sets of words by first character"""

    dictionary = {}
    with open(textfile, 'r') as word_file:
        for row in word_file:
            row = row.lower().rstrip()   # make entries case-insensitive

            dictionary.setdefault(row[0], set())
            vals = dictionary[row[0]]
            vals.add(row)
            dictionary[row[0]] = vals

        print "\nCreated dictionary."
        print "\n********************************"
    return dictionary


def make_letter_combinations(number):
    """Given a sequence of numbers on phonepad, returns all letter combinations.
    """

    combos = list(''.join(c) for c in itertools.product(*[phonepad[int(num)] for num in str(number)]))
    return combos


def generate_words(number_input, dictionary):
    """Prints list of words (if any) in dictionary, else prints number_input."""

    combos = make_letter_combinations(number_input)

    words_in_dict = [c for c in combos if c in dictionary[c[0]]]
    return words_in_dict if words_in_dict else number_input


def remove_non_lettered_characters(user_input):
    """Removes numerical input that doesn't have corresponding letters (0, 1).
    """

    letters_only = re.sub(r'[0-1]', "", user_input)
    return letters_only


def is_valid(user_input):
    """Returns False if user input includes nonnumeric characters."""

    invalid_input = re.findall(r'[^0-9]', user_input)
    return True if not invalid_input else False


def run():
    """Prompts user until user terminates program."""

    eng_dict = seed_dictionary(WORD_FILE)

    while True:
        user_input = raw_input("\nTo search dictionary words by phone number, "
                               + "enter 2 to 7 numbers between 0 and 9 and "
                               + "press enter.\nTo end the program, press "
                               + "enter.\n")
        if user_input:
            if is_valid(user_input):
                edited_input = remove_non_lettered_characters(user_input)
                if not edited_input:
                    print user_input
                else:
                    print generate_words(edited_input, eng_dict)
            else:
                print "\nPlease enter only numbers, or press enter to quit."
        else:
            print "You have ended the program.  Thank you!"
            break


if __name__ == '__main__':

    run()
