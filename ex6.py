#  assigns a string to variable x and assigns a format string integer
x = "There are %d types of people." % 10
#  assigns a string to variable binary
binary = "binary"
#  assigns a string to variable do_not
do_not = "don't"
#  assigns a string to variable y and assings a pair of format strings
y = "Those who know %s and those who %s."% (binary, do_not)

# prints the string called by variable x to the command line
print x
# prints the string called by the variable y to the command line
print y

# prints a string to the command line, calls format string called by variable x
print "I said: %r." % x
# prints a string to the command line, calls the format string called by variable y
print "I also said: '%s'." % y

# assigns boolean value false to the variable hilarious
hilarious = False
# assigns a string to the variable joke_evaluation which includes a raw format string
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the string called by the variable joke_evaluation to the command line
# prints the format string called by the variable hilarious to the command line
print joke_evaluation % hilarious

# assigns a string to the variable w
w = "This is the left side of..."
# assigns a string to the variable e
e = "a string with a right side."

# prints the strings called by the variables w and e to the command line
print w + e
