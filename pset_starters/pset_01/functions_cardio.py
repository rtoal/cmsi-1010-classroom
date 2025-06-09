# ----------------------------------------------------------------------
# This is the file functions_cardio.py
#
# The intent is to give you practice writing functions.
#
# Complete the functions below.
#
# Each function has a docstring that describes what it should do, but
# please see the unit tests at the bottom of the file for more
# specific examples of what each function should return. To run
# the tests, you can use the command
#
#     python3 -m unittest functions_cardio.py
#
# (or python depending on your system).
#
# Remove this comment, and all of the "replace the pass statement..."
# comments, prior to submission. You can, and should, add your own
# comments, but please remove all the comments that are here now.
# ----------------------------------------------------------------------

import unittest


def is_odd(n):
    """
    Returns True if n is odd, False otherwise.
    """
    # replace the pass statement with your code
    pass


def median_of_three(a, b, c):
    """
    Returns the median of three numbers a, b, and c.
    """
    # replace the pass statement with your code
    pass


def is_palindrome(s):
    """
    Returns True if the string s is a palindrome, False otherwise.

    A palindrome reads the same forwards and backwards. You can
    implement it as a simple check to see if s is equal to its
    reversal.
    """
    # replace the pass statement with your code
    pass


def factorial(n):
    """
    Returns the factorial of n (n!).

    The factorial of a non-negative integer n is the product of all
    positive integers less than or equal to n. Please implement this
    function with a for loop.
    """
    # replace the pass statement with your code
    pass


def count_of_latin_vowels(s):
    """
    Returns the number of vowels in the string s.

    The vowels are 'a', 'e', 'i', 'o', and 'u'. You can implement this
    function using a for loop to iterate through the string.
    """
    # replace the pass statement with your code
    pass


def longest_string(strings):
    """
    Returns the longest string from a list of strings.

    If there are multiple strings with the same maximum length, return
    the first one encountered.
    """
    # replace the pass statement with your code
    pass


def word_frequencies(s):
    """
    Returns a dictionary with the frequency of each word in the string s.
    The keys of the dictionary are the words, and the values are the
    number of times each word appears in the string.

    A word is defined as a sequence of characters separated by spaces.
    You can implement this function using the split method.
    """
    # replace the pass statement with your code
    pass


class TestFunctionsCardio(unittest.TestCase):
    def test_is_odd(self):
        self.assertTrue(is_odd(3))
        self.assertFalse(is_odd(8))
        self.assertTrue(is_odd(-3))
        self.assertFalse(is_odd(-8))

    def test_median_of_three(self):
        self.assertEqual(median_of_three(1, 2, 3), 2)
        self.assertEqual(median_of_three(10, 30, 20), 20)
        self.assertEqual(median_of_three(25, 15, 35), 25)
        self.assertEqual(median_of_three(900, 9999, -1050), 900)
        self.assertEqual(median_of_three(193, 191, 192.5), 192.5)
        self.assertEqual(median_of_three(99999, 0, -1000), 0)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(20), 2432902008176640000)

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("python"))

    def test_count_of_latin_vowels(self):
        self.assertEqual(count_of_latin_vowels("hello world"), 3)
        self.assertEqual(count_of_latin_vowels("aeiou"), 5)
        self.assertEqual(count_of_latin_vowels("xyz"), 0)
        self.assertEqual(count_of_latin_vowels("Python programming"), 4)
        self.assertEqual(count_of_latin_vowels("Aeiou"), 5)

    def test_longest_string(self):
        self.assertEqual(longest_string(
            ["apple", "banana", "cherry"]), "banana")
        self.assertEqual(longest_string(
            ["cat", "dog", "elephant"]), "elephant")
        self.assertEqual(longest_string(
            ["short", "longer", "longest"]), "longest")
        self.assertEqual(longest_string(["a", "ab", "abc"]), "abc")
        self.assertEqual(longest_string(
            ["one", "two", "three", "four"]), "three")

    def test_word_frequencies(self):
        self.assertEqual(
            word_frequencies("hello world hello"), {'hello': 2, 'world': 1})
        self.assertEqual(
            word_frequencies("a b a c b a"),
            {'a': 3, 'b': 2, 'c': 1})
        self.assertEqual(word_frequencies("test test test"), {'test': 3})
        self.assertEqual(word_frequencies(""), {})


if __name__ == "__main__":
    unittest.main()
