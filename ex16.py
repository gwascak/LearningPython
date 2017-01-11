# here we import the argument
from sys import argv
#here we define the argument, which will be a filename that we specify.
script, filename = argv
# Here's text we print out on the screen.  We call the variable "filename" from what we called it above.
print "We're going to erase %r" %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# Here the prompt stops and it waits for input from the user.
raw_input("?")
# Prints out text and then opens the file we created called "filename"
print "Opening the file..."
target = open(filename, 'w')
#prints again and then truncates the file called "filename"
print "Truncating the file. Goodbye!"
target.truncate()
# Prints out text
print "Now I'm going to ask you for three lines."
# asks us for three lines, waits for us to type something in as it's waiting for input.
line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")

print "I'm going to write these to the file."
# The target file called "filename" is still open and so we write the 3 lines to it.  Skipping spaces between.
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# Print out text and then we close the file called "filename"
print "And finally, we close it."
target.close()
