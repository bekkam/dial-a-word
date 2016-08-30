# Dail-A-Word
Dial-A-Word is a program which, given an input of numbers, maps numeric input to letters on a phonepad, and returns words found in a dictionary.  It uses words2.txt from https://github.com/dwyl/english-words/blob/master/words2.txt as a dictionary, and assumes you have saved words2.txt to its directory.


##### Time allocated:
At three hours, I had a working solution to the problem, albeit one that used recursion, and had poor runtime.  I spent another few hours tinkering with performance (testing different ways of creating the possible word combinations, and ways to structure the dictionary), refactoring, and writing tests.

##### Implementation:

Currently, I represent words2.txt as  a dictionary, with each letter of the alphabet representing a key, whose value is the set of all words that start with that letter.  Thus, searching for a term in words2.txt requires getting the term's first letter by indexing it at zero (O(1)), looking up the corresponding dictionary key (O(1)), and checking whether that term is a member of the set (worst case is O(n)). 

I use itertools.product to generate all possible letter sequences as a series of tuples, and call join on each tuple to create a string sequence.  Using itertools and a generator speeds up this calculation, simply due to how python is implemented under the hood. Moreover, because this calculation is not nested in a loop, it can be factored out into its own method, which makes for easier testing.


##### Usage:
To start program:

`python dial_a_word.py`

To run tests:

`python tests.py`

##### Thoughts on bonus options:
###### Additional Feature
An interesting feature that I would like to explore is making a webapp that searches for terms in a dictionary, and offers word completion options, similar Microsoft Word.  I suspect a prefix trie would be helpful, since one could explore all child nodes of the parent node that indicates the last letter of the word typed so far, and was looking into marisa tries prior to submitting this.


Aside from determining the appropriate data structure, another question I'd want to explore in building such an app would be how to quickly search, retrieve, and display word completion options to the user, so as to deliver a satisfactory experience.  I wonder if this could be handled with javascript/AJAX, or if something like React might produce better results.

###### Performance
In terms of performance, I'd like to experiment with trees and binary trees.  I wrote a version of the program that used binary search (because O(log (n)) runtime - yay!). Unfortunately, it did not pan out well because I forgot that in comparing two strings ("apple" < "banana"), python compares each character (so O(n), with n being the length of the string), which made my search O(n log(n)) for each possible letter sequence (ouch).

While the current implementation takes advantage of those features in python that are implemented more efficiently (generators, itertools, etc.), it does not take advantage of the fact that both words2.txt and the possible letter combinations are ordered alphabetically. Subsequent iterations would take advantage of this feature, as well as trees. 