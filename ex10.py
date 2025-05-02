#Escape characters
# \n newline
# \t Tab
# \\ Insert backslash
# \' Insert Single Quote
# \" Insert Double quote
# \r Carriage return - moves curser to the beginning of the line
# \b Backspace - moves cursor on space back
# \f Form feed - moves cursor to the next page
# \v Vertical tab - moves cursor vertical
# \xhh Hexadecimal - Represents a character using hex value hh

tabby_cat = "\t I'm tabbed in"
persian_cat = "I am split \n on a line"
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list: 
\t* Cat Food
\t\t** Fishies
\t\t\t***Catnip\n\t\t\t\t**** Grass
"""

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)
