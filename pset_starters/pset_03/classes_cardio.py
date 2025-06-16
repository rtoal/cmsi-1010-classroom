# ----------------------------------------------------------------------
# This is the file classes_cardio.py
#
# The intent is to give you practice with classes.
#
# Complete the functions below.
#
# There are no stubs in this file, so you will need to infer exactly
# how to write each class from the descriptions and the unit tests at
# the bottom of the file. To run the tests, you can use the command
#
#     python3 -m unittest data_structures_cardio.py
#
# (or python depending on your system).
#
# Remove this comment, and other comments serving as instructions,
# prior to submission. You can, and should, add your own comments,
# but please remove all the comments that are here now.
# ----------------------------------------------------------------------

import math
import io
from contextlib import redirect_stdout
import unittest


# Write a class called Rectangle, with attributes with and height,
# and methods to calculate the area and perimeter. The class should
# also have a __str__ method that returns a string representation
# of the rectangle in the format "Rectangle(width x height)".

# Write a class called Circle, with an attribute radius,
# and methods to calculate the area and circumference. The class
# should also have a __str__ method that returns a string
# representation of the circle in the format "Circle(radius=radius)".

# Write a class called Song, with attributes title, artist, and
# duration. The duration should be in seconds. The class should
# have a __str__ method that returns a string representation
# of the song in the format "title by artist (duration)s". The class
# should also have a method called play that PRINTS "Playing title
# by artist (duration)s".

# Write a class called Playlist, which contains a list of Song
# objects. The class should have methods to add a song, play all
# songs, and a __str__ method that returns a string representation
# of the playlist, with each song represented as "title by artist
# (duration)s" and separated by a pipe character (|). If the playlist
# is empty, the __str__ method should return "Playlist is empty.".

# Keep the following tests in your file. Use them as you do the
# work in this assignment.

class TestClassesCardio(unittest.TestCase):
    def test_rectangle(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12)
        self.assertEqual(rect.perimeter(), 14)
        self.assertEqual(str(rect), "Rectangle(3 x 4)")

    def test_circle(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 25*math.pi, places=5)
        self.assertAlmostEqual(circle.circumference(), 10*math.pi, places=5)
        self.assertEqual(str(circle), "Circle(radius=5)")

    def test_song(self):
        song = Song("Night Shift", "Lucy Dacus", 391)
        self.assertEqual(str(song), "Night Shift by Lucy Dacus (391s)")
        with io.StringIO() as captured_output:
            with redirect_stdout(captured_output):
                song.play()
            self.assertEqual(
                captured_output.getvalue(),
                "Playing Night Shift by Lucy Dacus (391s)\n")

    def test_playlist(self):
        playlist = Playlist()
        song1 = Song("Night Shift", "Lucy Dacus", 391)
        song2 = Song("I Was Neon", "Julia Jacklin", 243)
        song3 = Song("Forgiveness", "Alice Glass", 191)
        playlist.add_song(song1)
        playlist.add_song(song2)
        playlist.add_song(song3)
        self.assertEqual(
            str(playlist),
            "Night Shift by Lucy Dacus (391s)|"
            "I Was Neon by Julia Jacklin (243s)|"
            "Forgiveness by Alice Glass (191s)")
        with io.StringIO() as captured_output:
            with redirect_stdout(captured_output):
                playlist.play_all()
            self.assertEqual(
                captured_output.getvalue(),
                "Playing Night Shift by Lucy Dacus (391s)\n"
                "Playing I Was Neon by Julia Jacklin (243s)\n"
                "Playing Forgiveness by Alice Glass (191s)\n")
