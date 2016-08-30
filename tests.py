"""Test Suite for dial_a_word.py"""

import dial_a_word
import unittest


class DialAWordUtilityUnitTestCase(unittest.TestCase):
    """Unit tests for utility methods"""

    def test_valid_input(self):
        assert dial_a_word.is_valid('223') is True

    def test_should_disallow_punctuation(self):
        assert dial_a_word.is_valid('223!') is False

    def test_should_disallow_letters(self):
        assert dial_a_word.is_valid('as567dg') is False

    def test_remove_blank_characters(self):
        self.assertEqual(dial_a_word.remove_non_lettered_characters('0923'), '923')

    def test_return_empty_string_if_all_blank(self):
        self.assertEqual(dial_a_word.remove_non_lettered_characters('010'), '')


class DialAWordTestCase(unittest.TestCase):
    """Tests dial_a_word.py with dictionary and phonepad"""

    def setUp(self):
        self.eng_dict = dial_a_word.seed_dictionary(dial_a_word.WORD_FILE)
        self.phonepad = dial_a_word.phonepad

    def tearDown(self):
        print "Tear down complete."

    def test_letter_combinations(self):
        result = ['mj', 'mk', 'ml', 'nj', 'nk', 'nl', 'oj', 'ok', 'ol']
        self.assertEqual(dial_a_word.make_letter_combinations(65), result)

    def test_generate_words(self):
        self.assertEqual(dial_a_word.generate_words(333, self.eng_dict),
                         ['dee', 'fed', 'fee'])


if __name__ == '__main__':

    unittest.main()
