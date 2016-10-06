# Here we print out a line.
print "How old are you?",
# Here we define a variable called age and then we ask for the user to input info.
# That info is stored in the variable age.
age = raw_input()
# Here we print out a line.
print "How tall are you?",
# Here we define a variable called height and then we ask for the user to input info.
# That info is stored in the variable height.
height = raw_input()
# Here we print out a line.
print "How much do you weigh?",
# Here we define a variable called weight and then we ask for the user in input info.
# That info is stored in the variable weight.
weight = raw_input()

# Here we print a string where we use and call our variables defined above.
# The values that were typed in by the user are used for the value of the variables.
print "So, you're %r old, %r tall and %r heavy." % (
age, height, weight)
