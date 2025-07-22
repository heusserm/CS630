#command_line_roman_to_int.py
#An exploratory test harness for CS630, week 4, Assignment 1, SNHU
#----------------------------------------------------------#


from lib_roman_to_int import from_roman

while True:
    print("Input a roman numeral to convert to an integer, or Q to Quit:", end=" ")
    s = input()
    if s == "Q":
        print("Exiting; Goodbye!")
        print(" ")
        break
    result = from_roman(s)
    print("The result is " + str(result))
    print(" ")

