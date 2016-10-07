# We load the module argv again.
from sys import argv
# We ask for input when we run the script and we assign that to user_name.
script, user_name = argv
# We set a variable called prompt.
prompt = '# '

# Here we print a number of lines.
# Each line uses the input for the argument user_name.
# At the end we ask for user input and use the prompt variable.
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

# Here we print all 3 lines.
# We also use our raw_input from above.
print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have a %r computer.  Nice.
""" % (likes, lives, computer)
