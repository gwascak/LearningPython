# This first defines a variable called x that has a string.
x = "There are %d types of people." % 10
# Here we have two variables.
binary = "binary"
do_not = "don't"
# This first defines a variable called y that has a string.
y = "Those who know %s and those who %s" % (binary, do_not)

# Here we print both of the above variables.
print x
print y

# Here we print two strings that also call the variable x and y we created above.
print "I said: %r" % x
print "I also said: '%s'." % y

# Here we have two variables.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# Here we print our first variable and then print our second.
print joke_evaluation % hilarious

# We define two variables w and e.
w = "This is the left side of..."
e = "a string with a right side."

# Here we print the two variables.
print w + e
