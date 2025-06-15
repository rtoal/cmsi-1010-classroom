# ----------------------------------------------------------------------
# This is the file poker.py
#
# In this file, you will write a function that classifies poker hands,
# embedding it in a small application that deals hands and announces
# the type of hand for each player.
#
# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
#
# Things to do:
#
# This program will make use of the card.py module we created in Lab 11.
#
# In this file, your main program will first ask a user for a numbers
# of players, which should be between 2 and 10. Then it will deal that
# many hands of 5 cards each, using the deal() function from card.py.
# Then, for each hand, it will call a function called classify_hand()
# that you will write, which will classify the hand and return a string
# describing the hand. The classification should be one of the following:
#
#   - "High Card"
#   - "One Pair"
#   - "Two Pair"
#   - "Three of a Kind"
#   - "Straight"
#   - "Flush"
#   - "Full House"
#   - "Four of a Kind"
#   - "Straight Flush"
#   - "Royal Flush"
#
# The classification should be done according to the rules of poker, and
# you can find the rules online or in a book about poker. You should
# use the card.py module to help you with this.
# ----------------------------------------------------------------------
