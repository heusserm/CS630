# test_roman_to_int.py
#A code library for CS630, week 4, Assignment 1, SNHU
#By Matthew Heusser M.Heusser@snhu.edu Jun 2025
#----------------------------------------------------------#

# test_roman_to_int.py

from lib_roman_to_int import *

def test_from_roman_I_returns_1():
    assert roman_to_int.from_roman("I") == 1
