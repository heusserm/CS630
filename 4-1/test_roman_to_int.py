# test_roman_to_int.py
#A code library for CS630, week 4, Assignment 1, SNHU
#By Matthew Heusser M.Heusser@snhu.edu Jun 2025
#----------------------------------------------------------#

# test_roman_to_int.py

import roman_to_int

def test_from_roman_I_returns_1():
    assert roman_to_int.from_roman("I") == 1
    assert roman_to_int.from_roman("II") == 2
