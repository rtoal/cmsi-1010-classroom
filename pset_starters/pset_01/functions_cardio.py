# ----------------------------------------------------------------------
# This is the file functions_cardio.py

# The intent is to give you practice writing functions.

# Complete the functions below.
# Remove this comment when you have completed the functions.
# ----------------------------------------------------------------------

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


print(is_odd(3), " should be True")
print(is_odd(8), " should be False")
print(is_odd(-3), " should be True")
print(is_odd(-8), " should be False")

print(median_of_three(1, 2, 3), " should be 2")
print(median_of_three(1, 3, 2), " should be 2")
print(median_of_three(2, 1, 3), " should be 2")
print(median_of_three(2, 3, 1), " should be 2")
print(median_of_three(3, 1, 2), " should be 2")
print(median_of_three(3, 2, 1), " should be 2")

print(factorial(5), " should be 120")
print(factorial(0), " should be 1")
print(factorial(1), " should be 1")
print(factorial(6), " should be 720")
print(factorial(20), " should be 2432902008176640000")

print(is_palindrome("racecar"), " should be True")
print(is_palindrome("hello"), " should be False")
print(is_palindrome("madam"), " should be True")
print(is_palindrome("python"), " should be False")

print(count_of_latin_vowels("hello world"), " should be 3")
print(count_of_latin_vowels("aeiou"), " should be 5")
print(count_of_latin_vowels("xyz"), " should be 0")
print(count_of_latin_vowels("Python programming"), " should be 4")
print(count_of_latin_vowels("Aeiou"), " should be 5")

print(longest_string(["apple", "banana", "cherry"]), " should be banana")
print(longest_string(["cat", "dog", "elephant"]), " should be elephant")
print(longest_string(["short", "longer", "longest"]), " should be longest")
print(longest_string(["a", "ab", "abc"]), " should be abc")
print(longest_string(["one", "two", "three", "four"]), " should be three")

print(word_frequencies("hello world hello"),
      " should be {'hello': 2, 'world': 1}")
print(word_frequencies("Python is great Python"),
      " should be {'Python': 2, 'is': 1, 'great': 1}")
print(word_frequencies("a b a c b a"), " should be {'a': 3, 'b': 2, 'c': 1}")
print(word_frequencies("test test test"), " should be {'test': 3}")
print(word_frequencies(""), " should be {}")
