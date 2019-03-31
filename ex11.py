# prints a string to the command line
print "How old are you?",
# assigns a string to be input by the user to the variable age
age = raw_input()
# prints a string to the command line
# string should function as a prompt
print "How tall are you?",
# assings a string to be input by the user to the variable height
height = raw_input()
# prints a string to the command line
# string should function as a prompt
print "How much do you weigh?",
# assigns a string to be input by the user to the variable weight
weight = raw_input()

# prints a string to the command line that includes the prompt responses assigned to the variables age, height, and weight via format strings
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
