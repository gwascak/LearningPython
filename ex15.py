# This line imports an arguement that we type when running the script.
from sys import argv

script, filename = argv
# The arguement is the name of the file we created.
# Here it opens the file that we type in.
txt = open(filename)


# The line below prints out the text and our file name.
print "Here's your file %r" % filename
# This line reads the file and prints out it's content.
print txt.read()
# Added the below line which closes the variable txt.
txt.close()

# This prints the line below and requests the we input text.
# It asks for the name of the file again.
print "Type the filename again:"
file_again = raw_input("> ")

# This line opens the file again.
txt_again = open(file_again)


# This line prints out the contents of the file.
print txt_again.read()

# Added the below line which closes the variable txt_again.
txt_again.close()
