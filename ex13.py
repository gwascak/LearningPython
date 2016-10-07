# This lines imports the argv module.
from sys import argv
# Here we define the argv module.  We would need to add input for 4 argurments.
script, first, second, third, fourth = argv
# I've added raw_input asking what we should call this script.
stuff = raw_input("What is this called?")

# Here I've called the variable stuff from above.
# It takes the raw input and answers the question of "This script is called:"
print "This script is called:", stuff
# These 4 lines take the input from the 4 arguements we give and uses them at the end.
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your fourth variable is:", fourth
