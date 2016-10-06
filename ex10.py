
# Created threee variables.
# \t is a tab.
# \\ does a backslash.
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# Created another variable.
# \t does the tab.
# \n does a new line.
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# Here we print all of our variables out.
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Here I tried triple single-quotes instead of triple double-quotes.
# It appears to have the same effect.
dog = '''
This is a dog.
Dog's are not like cats.
\t* Dogs like sticks.
'''

print dog
