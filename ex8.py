# This defines a variable called formatter.  With a string.
formatter = "%r %r %r %r"

# Here we print the variable formatter and assign the values at the end.
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# Here we print the variable formatter and the assigned values are the variable.
print formatter % (formatter, formatter, formatter, formatter)
# Here we print formatter again and the assigned values are each of these lines of text.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight"
)
