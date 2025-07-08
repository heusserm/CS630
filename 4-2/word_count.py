#word_count.py
#A code library for CS630, week 4, Assignment 2, SNHU
#By Matthew Heusser M.Heusser@snhu.edu Jun 2025
#
#----------------------------------------------------------#

#----------------------------------------------------------#
def count_words(text: str) -> int:
#----------------------------------------------------------#
    """
    Counts the number of words in the input string.
    Words are defined as sequences of characters separated by whitespace.

    Args:
        text (str): The input string.

    Returns:
        int: The number of words in the string.
    """
    # Strip leading/trailing whitespace, then split on any whitespace
    # If the string is empty or only whitespace, split() returns []
    words = text.strip().split()
    return len(words)
